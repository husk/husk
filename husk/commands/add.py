from argparse import ArgumentParser
from husk.repo import Repo

__doc__ = """\
Adds a bundle to the repository specified by it's `path`. If `path`
is an existing directory/bundle, pass `--force` to register it with
the repository. Existing files of the same name will not be overwritten.
"""

parser = ArgumentParser(description=__doc__)

parser.add_argument('path', help='Path to bundle directory')
parser.add_argument('-r', '--repo', help='Path to Husk repository')


def main(options):
    repo = Repo(options.repo)
    repo.add_note(options.path)
