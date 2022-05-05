class Error(Exception):
    """Base class for other exceptions"""
    pass


class AmountTooSmallError(Error):
    pass


class AmountTooLargeError(Error):
    pass

class MultipleBetError(Error):
    pass

class BetDoesNotExistError(Error):
    pass