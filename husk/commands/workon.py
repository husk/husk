import os
import shlex
import subprocess
from husk.repo import Repo
from husk.exceptions import HuskError
from husk.decorators import cli


__doc__ = """\
Command to "work on" a bundle of files with the editor defined
in your Husk settings and falls back to what is set in the $EDITOR
environment variable.
"""


@cli(description=__doc__)
def parser(options):
    # Ensure this is a repository
    if not Repo.isrepo(options.repo):
        raise HuskError('{} is not a Husk repo'.format(options.repo))
    # Initialize a repo
    repo = Repo(options.repo)

    # Ensure the bundle exists before attempting to work on it
    if options.path not in repo.bundles:
        raise HuskError('{} bundle does not exist'.format(options.path))

    editor = repo.config.get('general', 'editor', os.environ.get('EDITOR'))

    if not editor:
        raise HuskError('Cannot open notes. The "general.editor" ' \
            'setting nor the $EDITOR environment variable are defined.')

    args = shlex.split(editor) + repo.bundles[options.path].files
    retcode = subprocess.call(args)

    if retcode != 0:
        raise HuskError('Editor had a non-successful exit. Nothing has been ' \
            'committed. To manually commit, use `husk commit`.')

    # TODO Commit it


parser.add_argument('path', help='Path to bundle directory')
parser.add_argument('-r', '--repo', default='.',
    help='Path to Husk repository')
