import os
import shlex
import subprocess
from husk.repo import Repo
from husk.exceptions import HuskError
from husk.decorators import cli


__doc__ = """\
Command to "work on" a note of files with the editor defined
in your Husk settings and falls back to what is set in the $EDITOR
environment variable.
"""


@cli(description=__doc__)
def parser(options):
    # No repo is explicitly defined, so find the closest one
    if not options.repo:
        options.repo = Repo.findrepo()

    # Ensure this is a repository
    if not Repo.isrepo(options.repo):
        raise HuskError('{} is not a Husk repo'.format(options.repo))

    # Initialize a repo
    repo = Repo(options.repo)

    path = os.path.relpath(os.path.join(os.getcwd(), options.path), repo.path)

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

    # TODO Commit it


parser.add_argument('path', help='Path to note directory')
parser.add_argument('files', nargs='*', help='Filenames to be opened')
parser.add_argument('-r', '--repo', help='Path to Husk repository')
