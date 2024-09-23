import os

from django.core.cache import cache
import logging

logging.basicConfig(level=os.getenv("LOG_LEVEL").upper())


def delete_cache(key):
    """
    Delete the cached data by key.
    Args:
        key (str): The cache key.
    """
    logging.warning(f"Cache evicted {key}")
    cache.delete(key)


def get_cache(key):
    """
    Get the cached data by key.
    Args:
        key (str): The cache key.
    Returns:
        Any: The cached data, or None if the key does not exist.
    """
    data = cache.get(key)

    if data:
        logging.info(f"Cache hit for {key}")
    else:
        logging.info(f"Cache miss for {key}")

    return data


def set_cache(key, value, timeout=600):
    """
    Set the cache with the given key and value.
    Args:
        key (str): The cache key.
        value (Any): The data to cache.
        timeout (int): Cache timeout in seconds (default is 10 minutes).
    """
    logging.info(f"cache set for {key}, timeout in {timeout} seconds")
    cache.set(key, value, timeout)
