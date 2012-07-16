import os
from argparse import ArgumentParser
from husk.config import HUSK_CONFIG_DIR


def init(path):
    config_path = os.path.join(path, HUSK_CONFIG_DIR)
    if os.path.exists(config_path):
        raise Exception('{} is already a Husk repository.'.format(path))
    os.makedirs(config_path)


parser = ArgumentParser()
parser.add_argument('-p', '--path', default='.', help='Path of Husk ' \
        'initialization. If no path is specified, the current working ' \
        'directory will be used.')


def main(options):
    init(options.path)
