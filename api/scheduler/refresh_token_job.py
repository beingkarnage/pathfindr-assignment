import logging
import os

from apscheduler.schedulers.background import BackgroundScheduler
from api.utils.refresh_token import refresh_token

logging.basicConfig(level=os.getenv("LOG_LEVEL").upper())


def start_scheduler():
    """
    Starts the scheduler for refreshing the token, defaults to 15 minutes

    """
    refresh_token()
    token_refresh_time = 15
    if os.getenv("REFRESH_TOKEN_SCHEDULER_TIME"):
        token_refresh_time = int(os.getenv("REFRESH_TOKEN_SCHEDULER_TIME"))

    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_token, 'interval', minutes=token_refresh_time)
    scheduler.start()
    logging.info("Background job for refreshing token is started")
