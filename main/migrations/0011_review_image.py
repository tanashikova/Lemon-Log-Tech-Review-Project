# Generated by Django 3.1.7 on 2021-03-20 20:22

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_merge_20210320_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]