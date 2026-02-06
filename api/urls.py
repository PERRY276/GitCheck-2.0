from django.urls import path
from .views import scan_repo, scan_history, index

urlpatterns = [
    path("", index),
    path("scan/", scan_repo),
    path("history/", scan_history),
]
