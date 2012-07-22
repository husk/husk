import os
from husk.repo import Repo
from husk.exceptions import HuskError
from husk.decorators import cli

__doc__ = """\
Moves an existing note to a new path.
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

    src = os.path.relpath(os.path.join(os.getcwd(), options.src), repo.path)
    dest = os.path.relpath(os.path.join(os.getcwd(), options.dest), repo.path)

    repo.notes.move(src, dest)


parser.add_argument('src', help='Source path to note that will be moved')
parser.add_argument('dest', help='Destination path of the note')
parser.add_argument('-r', '--repo', help='Path to Husk repository')
