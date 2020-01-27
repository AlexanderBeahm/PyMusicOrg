class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ConfigFormatError(Error):
    def __init__(self, configLine, message):
        self.configLine = configLine
        self.message = message