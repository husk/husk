from argparse import ArgumentParser
from husk.repo import Repo
from husk.config import HUSK_REPO_DIR


__doc__ = """\
Initialize a Husk repository in the current working directory (cwd)
unless a `path` is specified.
"""

parser = ArgumentParser(description=__doc__)

parser.add_argument('path', nargs='?', help='Path to Husk repository')
parser.add_argument('-a', '--add-config', action='store_true',
    help='Add a copy of the default config into the repo ' \
        '{} directory.'.format(HUSK_REPO_DIR))


def main(options):
    Repo.init(options.path, options.add_config)
