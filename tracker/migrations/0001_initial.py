# Generated by Django 5.2 on 2025-04-05 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TimeEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_name", models.CharField()),
                ("activity_name", models.CharField()),
                ("duration_minutes", models.IntegerField()),
                ("date", models.DateField()),
            ],
        ),
    ]
