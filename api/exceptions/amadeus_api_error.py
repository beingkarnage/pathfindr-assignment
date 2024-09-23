class AmadeusApiError(Exception):
    """Raised when calling the flight search api returned a not 200 response"""

    def __init__(self, params, message="Something went wrong while calling the flight search api {params}"):
        self.message = message.format(params=params)
        super().__init__(self.message)
