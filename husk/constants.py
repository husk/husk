from os import path, environ

__all__ = ('HUSK_CONTROL_DIR', 'HUSK_CONFIG_NAME', 'HUSK_NOTE_LOG_NAME',
    'HUSK_DEFAULT_CONFIG', 'HUSK_USER_CONFIG', 'HUSK_NOTE_FILES')

# Name of the directory that contains all the repo-specific files
# including log and configuration files
HUSK_CONTROL_DIR = '.husk'

HUSK_CONFIG_NAME = 'config'

# The `bundles` file is local to a repository and stores relative paths to
# all bundles in a repository.
HUSK_NOTE_LOG_NAME = 'notes'

# Absolute path to the default Husk config file
HUSK_DEFAULT_CONFIG = path.abspath(path.join(path.dirname(__file__),
    HUSK_CONFIG_NAME))

# Absolute path to the user-specific Husk config located in their
# home directory
HUSK_USER_CONFIG = path.abspath(path.join(environ['HOME'], '.huskconfig'))

# Names of files that are created within the bundle
HUSK_NOTE_FILES = ('outline', 'cues', 'summary')
