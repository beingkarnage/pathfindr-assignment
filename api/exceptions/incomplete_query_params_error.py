class IncompleteQueryParams(Exception):
    """Raised when incomplete query parameter received for flight search"""

    def __init__(self, params, message="Invalid query params received {params}"):
        self.message = message.format(params=params)
        super().__init__(self.message)
