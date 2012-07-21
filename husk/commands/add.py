from husk import Repo
from husk.exceptions import HuskError
from husk.decorators import cli

__doc__ = """\
Adds a bundle to the repository specified by it's `path`. If `path`
is an existing directory/bundle, pass `--force` to register it with
the repository. Existing files of the same name will not be overwritten.
"""


@cli(description=__doc__)
def parser(options):
    # Ensure this is a repository
    if not Repo.isrepo(options.repo):
        raise HuskError('{} is not a Husk repo'.format(options.repo))
    # Initialize a repo
    repo = Repo(options.repo)
    for path in options.path:
        # Create a bundle
        repo.bundles.add(path)


parser.add_argument('path', nargs='*', help='Path to bundle directory')
parser.add_argument('-r', '--repo', default='.',
    help='Path to Husk repository')
