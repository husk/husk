from argparse import ArgumentParser
from husk.repo import Repo
from husk.config import HUSK_REPO_DIR


parser = ArgumentParser()

parser.add_argument('path', nargs='?', help='Path to Husk repository')
parser.add_argument('-a', '--add-config', action='store_true',
    help='Add a copy of the default config into the repo ' \
        '{} directory.'.format(HUSK_REPO_DIR))


def main(options):
    Repo.init(options.path, options.add_config)
