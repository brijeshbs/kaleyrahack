# Generated by Django 4.1 on 2022-08-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_snacks_breakfast"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="admin",
            field=models.BooleanField(default=False),
        ),
    ]