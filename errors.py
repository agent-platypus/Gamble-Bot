class Error(Exception):
    """Base class for other exceptions"""
    pass


class BetTooSmallError(Error):
    pass


class BetTooLargeError(Error):
    pass

class MultipleBetError(Error):
    pass

class BetDoesNotExistError(Error):
    pass