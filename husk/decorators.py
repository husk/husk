def cached_property(func):
    cach_attr = '_{}'.format(func.__name__)

    @property
    def wrap(self):
        if not hasattr(self, cach_attr):
            value = func(self)
            if value is not None:
                setattr(self, cach_attr, value)
        return getattr(self, cach_attr, None)
    return wrap
