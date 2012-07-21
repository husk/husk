import os
from collections import OrderedDict
from .constants import HUSK_BUNDLE_FILES
from .exceptions import HuskError


class BundleLog(object):
    def __init__(self, path, extension):
        self.path = path.rstrip('/')
        self.extension = extension
        self._bundles = OrderedDict()

        # If this does exist, populate bundles
        if self.ondisk():
            self.fromdisk()

    def __contains__(self, key):
        "Proxy to internal bundles dict"
        return key.rstrip('/') in self._bundles

    def __getitem__(self, key):
        "Proxy to internal bundles dict"
        return self._bundles[key.rstrip('/')]

    def add(self, bundle):
        if not isinstance(bundle, Bundle) and isinstance(bundle, basestring):
            bundle = Bundle(bundle, self.extension)
        if bundle.path in self._bundles:
            raise HuskError('{} bundle already exists in this ' \
                'repo.'.format(bundle.path))
        self._bundles[bundle.path] = bundle

        # If on disk.. log immediately
        if self.ondisk():
            bundle.todisk()
            with open(self.path, 'a') as log:
                log.write('{}\n'.format(bundle.path))

    def ondisk(self):
        return os.path.exists(self.path)

    def todisk(self):
        with open(self.path, 'w') as log:
            for name in self._bundles:
                self._bundles[name].todisk()
                log.write('{}\n'.format(name))

    def fromdisk(self, force=False):
        if self._bundles and not force:
            raise HuskError('Fail to load from disk. Bundles already exist. ' \
                'Pass `force=True` to override.')
        with open(self.path) as log:
            for line in log.xreadlines():
                path = line.strip()
                self._bundles[path] = Bundle(path, self.extension)


class Bundle(object):
    def __init__(self, path, extension):
        self.path = path.rstrip('/')
        self.extension = extension

    def ondisk(self):
        return os.path.exists(self.path)

    def todisk(self):
        if not self.ondisk():
            os.makedirs(self.path)

        # Create empty files if they do not already exist
        for name in HUSK_BUNDLE_FILES:
            path = os.path.join(self.path, '{}.{}'.format(name, self.extension))
            if not os.path.exists(path):
                open(path, 'w').close()

    @property
    def files(self):
        # Create empty files if they do not already exist
        return [os.path.join(self.path, '{}.{}'.format(name, self.extension)) \
            for name in HUSK_BUNDLE_FILES]
