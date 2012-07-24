from husk import Repo
from husk.decorators import cli

__doc__ = """\
Remove a note from the specified repo. By default note files
are not deleted.
"""


@cli(description=__doc__)
def parser(options):
    # Find the nearest repo
    repo = Repo.findrepo(options.repo)

    for path in options.path:
        # Ensure the path is defined relative to the repo
        repo.notes.remove(repo.relpath(path), defer=True,
            delete=options.delete)
    repo.notes.todisk()


parser.add_argument('path', nargs='*', help='Path to note directory')
parser.add_argument('-r', '--repo', help='Path to Husk repository')
parser.add_argument('-d', '--delete', action='store_true',
    help='Delete note files from disk')
