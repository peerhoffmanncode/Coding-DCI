# Generated by Django 3.2.16 on 2023-01-04 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230104_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='houses',
            old_name='sate',
            new_name='state',
        ),
    ]
