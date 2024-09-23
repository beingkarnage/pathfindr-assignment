from django.apps import AppConfig
from api.scheduler.refresh_token_job import start_scheduler


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        start_scheduler()
