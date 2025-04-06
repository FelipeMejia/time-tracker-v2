from django import forms
from .models import TimeEntry


class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ["project_name", "activity_name", "duration_minutes", "date"]
