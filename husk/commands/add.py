from husk import Repo
from husk.decorators import cli

__doc__ = """\
Adds a note to the repository specified by it's `path`. If `path`
is an existing directory/note, pass `--force` to register it with
the repository. Existing files of the same name will not be overwritten.
"""


@cli(description=__doc__)
def parser(options):
    # Find the nearest repo
    repo = Repo.findrepo(options.repo)

    for path in options.path:
        # Ensure the path is defined relative to the repo
        repo.notes.add(repo.relpath(path), defer=True)
    repo.notes.todisk()


parser.add_argument('path', nargs='*', help='Paths to note directory')
parser.add_argument('-r', '--repo', help='Path to Husk repository')
parser.add_argument('-f', '--force', action='store_true',
    help='Force an existing unregistered note to be added to the repository')
