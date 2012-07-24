from husk import Repo
from husk.decorators import cli

__doc__ = """\
Shows various info about the repo.
"""


@cli(description=__doc__)
def parser(options):
    # Find the nearest repo
    repo = Repo.findrepo(options.repo)

    if 'notes' in options.stats:
        print('{} notes'.format(len(repo.notes)))
        print('-' * 5)
        for key in repo.notes:
            print(repo.relpath(key))


parser.add_argument('stats', nargs='*', default='notes',
    choices=['notes'], help='Specify which kinds of info to be presented')
parser.add_argument('-r', '--repo', help='Path to Husk repository')
