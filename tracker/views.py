from django.shortcuts import render, redirect
from .forms import TimeEntryForm
from .models import TimeEntry
from datetime import datetime
from collections import defaultdict


# Create your views here.
def log_time_entry(request):
    if request.method == "POST":
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = TimeEntryForm()
    return render(request, "log_time_entry.html", {"form": form})


def success_view(request):
    return render(request, "success.html")


def weekly_summary_view(request):
    entries = TimeEntry.objects.all().order_by("date")
    summary = defaultdict(lambda: defaultdict(int))

    for entry in entries:
        week_number = entry.date.isocalendar()[1]
        summary[week_number][entry.project_name] += entry.duration_minutes

    summary_data = []
    for week, projects in summary.items():
        summary_data.append(
            {
                "week": week,
                "projects": [
                    {"name": name, "duration": duration}
                    for name, duration in projects.items()
                ],
            }
        )

    return render(request, "weekly_summary.html", {"summary_data": summary_data})
