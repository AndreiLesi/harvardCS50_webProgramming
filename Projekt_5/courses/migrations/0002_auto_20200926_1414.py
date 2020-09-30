# Generated by Django 3.1.1 on 2020-09-26 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='enrolled',
            field=models.ManyToManyField(blank=True, default=0, related_name='students', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploadedCourses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='isLiked', to='courses.Course'),
        ),
    ]