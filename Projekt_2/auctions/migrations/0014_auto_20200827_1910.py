# Generated by Django 3.1 on 2020-08-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20200821_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Books', 'Books'), ('Technology', 'Technology'), ('Home', 'Home'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Fashion', 'Fashion'), ('Other', 'Other')], max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]
