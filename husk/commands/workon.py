import os
import shlex
import subprocess
from husk import Repo, HuskError
from husk.decorators import cli

__doc__ = """\
Command to "work on" a note of files with the editor defined
in your Husk settings and falls back to what is set in the $EDITOR
environment variable.
"""


@cli(description=__doc__)
def parser(options):
    # Find the nearest repo
    repo = Repo.findrepo(options.repo)

    # Adjust path
    path = repo.relpath(options.path)

    # Ensure the note exists before attempting to work on it
    if path not in repo.notes:
        raise HuskError('{} note does not exist'.format(path))

    editor = repo.config.get('general', 'editor', os.environ.get('EDITOR'))

    if not editor:
        raise HuskError('Cannot open notes. The "general.editor" ' \
            'setting nor the $EDITOR environment variable are defined.')

    args = shlex.split(editor) + repo.notes[path].files
    retcode = subprocess.call(args)

    if retcode != 0:
        raise HuskError('Editor had a non-successful exit. Nothing has been ' \
            'committed. To manually commit, use `husk commit`.')


parser.add_argument('path', help='Path to note directory')
parser.add_argument('files', nargs='*', help='Filenames to be opened')
parser.add_argument('-r', '--repo', help='Path to Husk repository')
