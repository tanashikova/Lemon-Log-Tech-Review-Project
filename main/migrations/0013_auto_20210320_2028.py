# Generated by Django 3.1.7 on 2021-03-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210320_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True, unique_for_date='publish'),
        ),
    ]
