class InvalidPRException(Exception):
    """
    Exception raised for an invalid press release.

    Attributes:
        press_release -- invalid press release
        message -- exception message
    """

    def __init__(self, press_release, message="Press release is invalid.") -> None:
        self.press_release = press_release
        self.message = message

        super().__init__(self.message)


class InvalidPRDateException(Exception):
    """
    Exception raised for an invalid press release date.

    Attributes:
        press_release -- invalid press release
        message -- exception message
    """

    def __init__(self, press_release, message="Press release date is invalid.") -> None:
        self.press_release = press_release
        self.message = message

        super().__init__(self.message)