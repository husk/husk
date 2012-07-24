from husk import Repo
from husk.decorators import cli

__doc__ = """\
Moves an existing note to a new path.
"""


@cli(description=__doc__)
def parser(options):
    # Find the nearest repo
    repo = Repo.findrepo(options.repo)

    src = repo.relpath(options.src)
    dest = repo.relpath(options.dest)
    repo.notes.move(src, dest)


parser.add_argument('src', help='Source path to note that will be moved')
parser.add_argument('dest', help='Destination path of the note')
parser.add_argument('-r', '--repo', help='Path to Husk repository')
