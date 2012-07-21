from husk.repo import Repo
from husk.decorators import cli

__doc__ = """\
Initialize a Husk repository in the current working directory (cwd)
unless a `path` is specified.
"""


@cli(description=__doc__)
def parser(options):
    Repo.init(options.path, options.defaults)


parser.add_argument('path', nargs='?', default='.',
    help='Path to Husk repository')
parser.add_argument('-d', '--defaults', action='store_true',
    help='Add a copy of the Husk defaults to the repo control directory.')
