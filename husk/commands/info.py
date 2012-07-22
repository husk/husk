import os
from husk.repo import Repo
from husk.exceptions import HuskError
from husk.decorators import cli


__doc__ = """\
Shows various info about the repo.
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

    if 'notes' in options.stats:
        print('{} notes'.format(len(repo.notes)))
        print('-' * 5)
        for key in repo.notes:
            print(os.path.join(os.path.relpath(repo.path, '.'), key))


parser.add_argument('stats', nargs='*', default='notes',
    choices=['notes'], help='Specify which kinds of info to be presented')
parser.add_argument('-r', '--repo', help='Path to Husk repository')
