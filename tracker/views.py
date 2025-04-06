from django.shortcuts import render, redirect
from .forms import TimeEntryForm


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
