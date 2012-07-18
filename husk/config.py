import os
from ConfigParser import ConfigParser
from husk import utils
from husk.exceptions import HuskError, HuskConfigError
from husk.decorators import cached_property

__all__ = ['ConfigParser', 'get_config']


HUSK_REPO_DIR = '.husk'
HUSK_CONFIG_NAME = 'config'

HUSK_DEFAULT_CONFIG = os.path.abspath(os.path.join(os.path.dirname(__file__),
    HUSK_CONFIG_NAME))
HUSK_USER_CONFIG = os.path.join(os.environ['HOME'], '.huskconfig')
HUSK_REPO_CONFIG = os.path.join(HUSK_REPO_DIR, HUSK_CONFIG_NAME)


# Map of config attributes and their intended types
_config_types = {
    'notifications': {
        'enabled': bool,
        'days': int,
        'weeks': int,
        'years': int,
    }
}


class HuskConfigSection(object):
    pass


class HuskConfig(object):
    def __init__(self, path):
        self.path = path
        self.repo_config = os.path.join(path, HUSK_REPO_CONFIG)

        # Convert each section into an object and coerce set it locally
        for name in self.parser.sections():
            options = HuskConfigSection()
            types = _config_types.get(name, {})
            for key, value in self.parser.items(name):
                if key in types:
                    try:
                        value = types[key](value)
                    except (TypeError, ValueError):
                        error = 'Invalid value in the "{}" section. ' \
                            'Parameter "{}" should be type {}'
                        raise HuskConfigError(error.format(name, key,
                            types[key].__name__))
                setattr(options, key.replace('-', '_'), value)
            setattr(self, name.replace('-', '_'), options)

    @cached_property
    def parser(self):
        parser = ConfigParser()
        # Right-most takes precedence..
        parser.read([HUSK_DEFAULT_CONFIG, HUSK_USER_CONFIG, self.repo_config])
        return parser


def init_config(path, add_config=False):
    if not os.path.isdir(path):
        raise HuskConfigError('{} is not a directory.'.format(path))
    if os.path.exists(os.path.join(path, HUSK_REPO_DIR)):
        raise HuskConfigError('{} is already a Husk repository.'.format(path))

    os.makedirs(os.path.join(path, HUSK_REPO_DIR))

    if add_config:
        default_config = open(HUSK_DEFAULT_CONFIG)
        repo_config = open(HuskConfig(path).repo_config, 'w')
        repo_config.write(default_config.read())
        repo_config.close()
        default_config.close()


def get_config(path=None):
    """Returns a HuskConfig instance for the current repo.

    This starts in the `cwd` and walks up the tree until the repo
    config is found. This enables the flexibility of being in any
    subdirectory and still be able to access the repo config.
    """
    path = utils.parent_dir(HUSK_REPO_DIR, path)
    if path:
        return HuskConfig(path)
    raise HuskError('Not a Husk repository (or any of the parent '
        'directories). Use `husk init` to create a new repository.')
