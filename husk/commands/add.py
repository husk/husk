from argparse import ArgumentParser
from husk.repo import Repo


parser = ArgumentParser()

parser.add_argument('path', help='Path to notes directory')
parser.add_argument('-r', '--repo', help='Path to Husk repository')


def main(options):
    repo = Repo(options.repo)
    repo.add_note(options.path)
