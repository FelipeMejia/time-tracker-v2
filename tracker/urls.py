from django.urls import path
from . import views

urlpatterns = [
    path("log/", views.log_time_entry, name="log_time_entry"),
    path("success/", views.success_view, name="success"),
]
