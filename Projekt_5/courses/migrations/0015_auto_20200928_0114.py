# Generated by Django 3.1.1 on 2020-09-27 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20200927_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='lengthWeeks',
            new_name='length',
        ),
    ]
