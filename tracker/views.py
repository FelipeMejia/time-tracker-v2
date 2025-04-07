from django.shortcuts import render, redirect
from .forms import TimeEntryForm
from .utils import get_weekly_summary
from django.http import JsonResponse


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
    summary_data = get_weekly_summary()
    return render(request, "weekly_summary.html", {"summary_data": summary_data})


def weekly_summary_api_review(request):
    summary_data = get_weekly_summary()
    return JsonResponse({"summary_data": summary_data})
