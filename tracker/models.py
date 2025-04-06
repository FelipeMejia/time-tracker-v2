from django.db import models


class TimeEntry(models.Model):
    project_name = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.project_name
