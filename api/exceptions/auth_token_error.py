class AuthTokenError(Exception):
    """ Raised when the authentication token is not present """
    def __init__(self, message="Unable to get the auth token from cache"):
        self.message = message
        super().__init__(self.message)
