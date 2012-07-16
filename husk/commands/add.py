import os
from argparse import ArgumentParser
from husk.config import check_config


parser = ArgumentParser()

parser.add_argument('path', help='Path to notes directory')
parser.add_argument('-d', '--desc', help='Short description of notes')


def add(path):
    config = check_config()
    abspath = os.path.join(config.path, path)
    if os.path.exists(abspath):
        raise IOError('Directory already exists')
    os.makedirs(abspath)
    open(os.path.join(abspath, 'notes.txt'), 'w').close()
    open(os.path.join(abspath, 'cues.txt'), 'w').close()
    open(os.path.join(abspath, 'summary.txt'), 'w').close()


def main(options):
    add(options.path)
