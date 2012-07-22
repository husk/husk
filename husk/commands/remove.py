from husk.repo import Repo
from husk.exceptions import HuskError
from husk.decorators import cli

__doc__ = """\
Remove a note from the specified repo. By default note files
are not deleted.
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
    for path in options.path:
        # Ensure the path is defined relative to the repo
        repo.notes.remove(repo.relpath(path), defer=True,
            delete=options.delete)
    repo.notes.todisk()


parser.add_argument('path', nargs='*', help='Path to note directory')
parser.add_argument('-r', '--repo', help='Path to Husk repository')
parser.add_argument('-d', '--delete', action='store_true',
    help='Delete note files from disk.')
