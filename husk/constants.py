from os import path, environ

# Name of the directory that contains all the repo-specific files
# including log and configuration files
HUSK_CONTROL_DIR = '.husk'

HUSK_CONFIG_NAME = 'config'

# The `bundles` file is local to a repository and stores relative paths to
# all bundles in a repository.
HUSK_BUNDLE_LOG_NAME = 'bundles'

# Absolute path to the default Husk config file
HUSK_DEFAULT_CONFIG = path.abspath(path.join(path.dirname(__file__),
    HUSK_CONFIG_NAME))

# Absolute path to the user-specific Husk config located in their
# home directory
HUSK_USER_CONFIG = path.abspath(path.join(environ['HOME'], '.huskconfig'))

# Names of files that are created within the bundle
HUSK_BUNDLE_FILES = ('outline', 'cues', 'summary')
