import os
from husk.exceptions import HuskConfigError
from husk.config import HUSK_REPO_DIR, HUSK_DEFAULT_CONFIG, HuskConfig, get_config


def repo_exists(path):
    return os.path.exists(os.path.join(path, HUSK_REPO_DIR))


class Repo(object):
    def __init__(self, path):
        self.config = get_config()

    @classmethod
    def init(cls, path, add_config=False):
        """Initializes a repo within the supplied path. Optionally add a copy
        of the default config into the repo.
        """
        if not os.path.isdir(path):
            raise HuskConfigError('{} is not a directory.'.format(path))
        if repo_exists(path):
            raise HuskConfigError('{} is already a Husk repository.'.format(path))
        os.makedirs(os.path.join(path, HUSK_REPO_DIR))

        if add_config:
            default_config = open(HUSK_DEFAULT_CONFIG)
            repo_config = open(HuskConfig(path).repo_config, 'w')
            repo_config.write(default_config.read())
            repo_config.close()
            default_config.close()
        return cls(path)
