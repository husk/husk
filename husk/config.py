import os
from ConfigParser import ConfigParser, NoOptionError
from .constants import HUSK_DEFAULT_CONFIG, HUSK_USER_CONFIG
from .exceptions import HuskError, HuskConfigError
from .decorators import cached_property

__all__ = ('Config', 'default_config')

noop = lambda x: x

# Map of config attributes and their intended types
config_types = {
    'notifications': {
        'enabled': bool,
        'days': int,
        'weeks': int,
        'years': int,
    }
}


class Config(object):
    """The Husk configuration class.

    If the init `path` exists and can be parsed, the settings will be
    read in and used.
    """
    def __init__(self, path=None):
        if isinstance(path, basestring):
            path = path.rstrip('/')
        self.path = path

    @classmethod
    def write_defaults(cls, path):
        "Write a copy of the default config to the specified file."
        if os.path.exists(path):
            raise HuskError('Cannot write default config, file already exists.')
        copy = open(path, 'w')
        default = open(HUSK_DEFAULT_CONFIG)
        copy.write(default.read())
        default.close()
        copy.close()

    @cached_property
    def parser(self):
        parser = ConfigParser()
        # Right-most takes precedence..
        parser.read([HUSK_DEFAULT_CONFIG, HUSK_USER_CONFIG, self.path])
        return parser

    def ondisk(self):
        return os.path.exists(self.path)

    def get(self, section, key, default=None):
        types = config_types.get(section, {})
        if self.parser.has_section(section):
            try:
                value = self.parser.get(section, key)
                return types.get(key, noop)(value)
            except NoOptionError:
                pass
            except (TypeError, ValueError):
                raise HuskConfigError('Invalid value in the "{}" section. ' \
                    'Parameter "{}" should be type {}'.format(section, key,
                        types[key].__name__))
        return default

    def set(self, section, key, value):
        "Set a config setting."
        if self.path is None:
            raise HuskError('Cannot set config. No repo config defined.')
        if not self.parser.has_section(section):
            self.parser.add_section(section)
        self.parser.set(section, key, value)

    def unset(self, section, key):
        "Unset a config setting."
        if self.path is None:
            raise HuskError('Cannot unset config. No repo config defined.')
        if self.parser.has_section(section):
            return self.parser.remove_option(section, key)
        return False

    def todisk(self):
        if self.path is None:
            raise HuskError('Cannot write to disk. No repo config defined.')
        with open(self.path) as config:
            self.parser.write(config)


def default_config():
    return Config()
