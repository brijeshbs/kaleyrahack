# Generated by Django 4.1 on 2022-08-23 21:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_user_admin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="breakfast",
            name="dateOfEntry",
            field=models.DateField(default=datetime.date(2022, 8, 24)),
        ),
        migrations.AlterField(
            model_name="snacks",
            name="dateOfEntry",
            field=models.DateField(default=datetime.date(2022, 8, 24)),
        ),
    ]
