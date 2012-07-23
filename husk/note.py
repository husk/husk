import os
from collections import OrderedDict
from .config import default_config
from .constants import HUSK_NOTE_FILES
from .exceptions import HuskError

__all__ = ('Notes', 'Note')


class Notes(object):
    "dict-like container for managing multiple notes."
    def __init__(self, path, extension=None):
        if extension is None:
            extension = default_config().get('general', 'extension')
        self.path = path.rstrip('/')
        self.extension = extension

        self._notes = OrderedDict()

        # If this does exist, populate notes
        if self.ondisk():
            self.fromdisk()

    def __iter__(self):
        "Proxy to internal notes dict"
        for key in self._notes:
            yield key

    def __len__(self):
        "Proxy to internal notes dict"
        return len(self._notes)

    def __contains__(self, key):
        "Proxy to internal notes dict"
        if isinstance(key, basestring):
            key = key.rstrip('/')
        return key in self._notes

    def __getitem__(self, key):
        "Proxy to internal notes dict"
        if isinstance(key, basestring):
            key = key.rstrip('/')
        return self._notes[key]

    def add(self, note, defer=False):
        if not isinstance(note, Note):
            note = Note(note, self.extension)

        if note.path in self._notes:
            raise HuskError('{} note already exists in this ' \
                'repo.'.format(note.path))

        self._notes[note.path] = note

        # If on disk.. log immediately
        if self.ondisk():
            note.todisk()
            if not defer:
                with open(self.path, 'a') as log:
                    log.write('{}\n'.format(note.path))

    def remove(self, note, delete=False, defer=False):
        """Removes a note from the repo.

        If `rmdisk` is True, the note is removed from disk as well.
        If `defer` is True, the notelog will not be updated. This
        is useful to prevent redundant IO in a tight loop.
        """
        if not isinstance(note, Note):
            note = Note(note, self.extension)

        if note.path not in self._notes:
            raise HuskError('{} note does not exist in this ' \
                'repo.'.format(note.path))

        del self._notes[note.path]

        # If on disk.. log immediately
        if self.ondisk():
            if delete:
                note.rmdisk()
            if not defer:
                self.todisk()

    def move(self, note, target, defer=False):
        """Moves a note from it's current path to a different path."

        If `defer` is True, the notelog will not be updated. This
        is useful to prevent redundant IO in a tight loop.
        """
        if not isinstance(note, Note):
            note = Note(note, self.extension)

        if note.path not in self._notes:
            raise HuskError('{} note does not exist in this ' \
                'repo.'.format(note.path))

        # Ensure the target is not an existing note
        if target in self._notes:
            raise HuskError('{} already exists.'.format(target))

        # Reference old path
        source = note.path

        # If on disk.. perist to disk
        if self.ondisk():
            note.mvdisk(target)
            # Internally change after a succesful move occurred
            # to prevent inconsistencies
            del self._notes[source]
            self._notes[note.path] = note
            if not defer:
                self.todisk()
        else:
            note.path = target
            del self._notes[source]
            self._notes[target] = note

    def ondisk(self):
        return os.path.exists(self.path)

    def todisk(self):
        with open(self.path, 'w') as log:
            for name in self._notes:
                self._notes[name].todisk()
                log.write('{}\n'.format(name))

    def fromdisk(self, force=False):
        if len(self) and not force:
            raise HuskError('Fail to load from disk. Notes already exist. ' \
                'Pass `force=True` to override.')
        with open(self.path) as log:
            for line in log.xreadlines():
                path = line.strip()
                self._notes[path] = Note(path, self.extension)


class Note(object):
    def __init__(self, path, extension):
        self.path = path.rstrip('/')
        self.extension = extension

    def ondisk(self):
        return os.path.exists(self.path)

    def todisk(self):
        if not self.ondisk():
            os.makedirs(self.path)

        # Create empty files if they do not already exist
        for name in HUSK_NOTE_FILES:
            path = os.path.join(self.path, '{}.{}'.format(name, self.extension))
            if not os.path.exists(path):
                open(path, 'w').close()

    def rmdisk(self):
        # Remove known files
        for name in self.files:
            os.remove(name)

        # Attempt to remove all directories including leaf. OSError is
        # only raised if the leaf cannot be removed. Errors for attempting
        # to remove parent directories are ignored
        try:
            os.removedirs(self.path)
        except OSError:
            print('{} is not empty, not removing'.format(self.path))

    def mvdisk(self, target):
        if self.ondisk():
            os.renames(self.path, target)
        self.path = target

    @property
    def files(self, names=None):
        names = names or HUSK_NOTE_FILES
        # Create empty files if they do not already exist
        return [os.path.join(self.path, '{}.{}'.format(name, self.extension)) \
            for name in names if name in HUSK_NOTE_FILES]
