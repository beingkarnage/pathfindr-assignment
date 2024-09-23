def generate_flight_cache_key(origin, destination, date):
    """
    generates the key for cache
    Args:
        origin: (str) origin location code
        destination: (str) destination location code
        date: (str or date) date of departure
    returns: (str) with prefix of `flight_`
    """
    return f"flight_{origin}_{destination}:{date}"
