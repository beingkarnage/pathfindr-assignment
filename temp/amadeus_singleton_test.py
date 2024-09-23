from random import randint


class AmadeusAPIConfig:
    _instance = None

    def __init__(self):
        self.amadeus_api_key = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AmadeusAPIConfig, cls).__new__(cls)
        return cls._instance

    def get_api_key(self):
        if self.amadeus_api_key is None:
            # fetch api key
            self.amadeus_api_key = randint(1, 10)
        return self.amadeus_api_key


