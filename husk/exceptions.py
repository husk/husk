__all__ = ('HuskError', 'HuskConfigError')


class HuskError(Exception):
    pass


class HuskConfigError(HuskError):
    pass
