# Generated by Django 3.1.1 on 2020-09-27 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20200927_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='courseSummary',
            new_name='summary',
        ),
    ]
