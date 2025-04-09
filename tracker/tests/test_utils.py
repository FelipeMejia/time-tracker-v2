import pytest
from tracker.models import TimeEntry
from tracker.utils import get_weekly_summary
from datetime import date


@pytest.mark.django_db
def test_get_weekly_summary_returns_correct_grouping():
    # Week 14
    TimeEntry.objects.create(
        project_name="A",
        activity_name="Design",
        duration_minutes=30,
        date=date(2025, 4, 1),
    )
    TimeEntry.objects.create(
        project_name="A",
        activity_name="Design",
        duration_minutes=45,
        date=date(2025, 4, 2),
    )

    # Week 15
    TimeEntry.objects.create(
        project_name="B",
        activity_name="Build",
        duration_minutes=20,
        date=date(2025, 4, 10),
    )

    summary = get_weekly_summary()

    assert isinstance(summary, list)
    assert len(summary) == 2  # 2 weeks

    week_14 = next(item for item in summary if item["week"] == 14)
    week_15 = next(item for item in summary if item["week"] == 15)

    assert any(p["name"] == "A" and p["duration"] == 75 for p in week_14["projects"])
    assert any(p["name"] == "B" and p["duration"] == 20 for p in week_15["projects"])
