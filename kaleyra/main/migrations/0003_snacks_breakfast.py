# Generated by Django 4.1 on 2022-08-23 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_user_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Snacks",
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
                (
                    "dateOfEntry",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="snacks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Breakfast",
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
                (
                    "dateOfEntry",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="breakfasts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
