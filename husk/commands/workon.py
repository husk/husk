import os
import shlex
import subprocess
from argparse import ArgumentParser
from husk.repo import Repo
from husk.exceptions import HuskError


parser = ArgumentParser()

parser.add_argument('path', help='Path to notes directory')
parser.add_argument('-r', '--repo', help='Path to Husk repository')


def main(options):
    repo = Repo(options.repo)
    editor = repo.config.general.editor or os.environ.get('EDITOR')

    if not editor:
        raise HuskError('Cannot open notes. The "general.editor" ' \
            'parameter nor the $EDITOR environment variable defined.')
    args = shlex.split(editor) + repo.get_files(options.path)
    retcode = subprocess.call(args)

    if retcode != 0:
        raise HuskError('Editor had a non-successful exit. Nothing has been ' \
            'committed. To manually commit, use `husk commit`.')

    # TODO Commit it
