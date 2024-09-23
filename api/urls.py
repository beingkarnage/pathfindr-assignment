from django.urls import path
from api.views import flights, ping

urlpatterns = [
    path("flights/price", flights),
    path("flights/ping", ping)
]
