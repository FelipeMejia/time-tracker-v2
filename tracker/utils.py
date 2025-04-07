from .models import TimeEntry
from collections import defaultdict


def get_weekly_summary():
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
    return summary_data
