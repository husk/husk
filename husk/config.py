import os

HUSK_CONFIG_DIR = '.husk'


class HuskConfig(object):
    def __init__(self, path):
        self.path = path
        self.config_path = os.path.join(path, HUSK_CONFIG_DIR)

    @property
    def logfile(self):
        return open(os.path.join(self.config_path, '.log'), 'w+')


def check_config():
    "Ensure the cwd has a husk directory."
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        if HUSK_CONFIG_DIR in dirs:
            return HuskConfig(root)
    raise Exception('Not a Husk repository (or any of the parent '
        'directories). Use `husk init` to create a new repository.')
