import os
from .exceptions import HuskError
from .constants import (HUSK_CONTROL_DIR, HUSK_CONFIG_NAME,
    HUSK_NOTE_LOG_NAME)
from .config import Config
from .note import Notes

__all__ = ('Repo',)


class Repo(object):
    def __init__(self, path):
        self.path = os.path.abspath(path.rstrip('/'))
        self.config = Config(os.path.join(self.controldir, HUSK_CONFIG_NAME))
        self.notes = Notes(os.path.join(self.controldir,
            HUSK_NOTE_LOG_NAME), extension=self.config.get('general', 'extension'))

    @classmethod
    def isrepo(cls, path):
        "Checks if a `path` is an existing Husk repo."
        return os.path.exists(os.path.join(path, HUSK_CONTROL_DIR))

    @classmethod
    def findrepo(cls, path=None):
        path = path or os.getcwd()
        while True:
            if Repo.isrepo(path):
                return Repo(path)
            # No where else to go, break the loop
            if path == '/':
                raise HuskError('Repo does not exist in current directory ' \
                    'or any parent directory.')
            path = os.path.dirname(path)

    @classmethod
    def init(cls, path, defaults=False):
        "Shorthand method for initializing and writing to disk."
        # Ensure this is not an existing repo
        if cls.isrepo(path):
            raise HuskError('{} is already a Husk repository.'.format(path))

        repo = cls(path)
        repo.todisk(defaults)
        return repo

    @property
    def controldir(self):
        return os.path.join(self.path, HUSK_CONTROL_DIR)

    def relpath(self, path):
        "Returns a path relative to this repo given `path`."
        return os.path.relpath(os.path.join(os.getcwd(), path), self.path)

    def ondisk(self):
        "Returns whether this repo exists on disk."
        return os.path.exists(self.controldir)

    def todisk(self, defaults=False):
        "Writes the repo to disk."
        if not self.ondisk():
            # Make all directories up the control directory
            os.makedirs(self.controldir)

            if defaults:
                Config.write_defaults(self.config.path)
            self.notes.todisk()
