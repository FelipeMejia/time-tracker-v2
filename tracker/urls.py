from django.urls import path
from . import views

urlpatterns = [
    path("log/", views.log_time_entry, name="log_time_entry"),
    path("success/", views.success_view, name="success"),
    path("summary/", views.weekly_summary_view, name="weekly_summary"),
    path(
        "api/weekly-summary/",
        views.weekly_summary_api_review,
        name="weekly_summary_api",
    ),
]
