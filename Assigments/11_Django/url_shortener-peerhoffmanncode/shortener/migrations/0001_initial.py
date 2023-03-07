# Generated by Django 4.1.6 on 2023-02-03 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Url",
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
                ("source_url", models.CharField(max_length=255, unique=True)),
                ("short_url", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("expires", models.DateTimeField(default=datetime.date(2023, 2, 17))),
            ],
        ),
    ]