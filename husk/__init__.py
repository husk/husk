from argparse import ArgumentParser
from .commands import init, add, workon, log, info, commit


__version__ = '0.1a'

# Available top-level commands
commands = {
    'init': init,
    'add': add,
    'workon': workon,
    'log': log,
    'info': info,
    'commit': commit,
}

# Top-level argument parser
parser = ArgumentParser(version='Husk v{}'.format(__version__))

# Add sub-parsers for each command
subparsers = parser.add_subparsers(dest='command')

# Populate subparsers
for name in commands:
    module = commands[name]
    parents = []
    if hasattr(module, 'parser'):
        subparsers.add_parser(name, parents=[module.parser], add_help=False)


def main(options):
    module = commands[options.command]
    try:
        module.main(options)
    except Exception, e:
        parser.error(e.message)
