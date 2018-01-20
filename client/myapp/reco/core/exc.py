"""reco exception classes."""

class recoError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class recoConfigError(recoError):
    """Config related errors."""
    pass

class recoRuntimeError(recoError):
    """Generic runtime errors."""
    pass

class recoArgumentError(recoError):
    """Argument related errors."""
    pass
