# Generated by Django 5.0.6 on 2024-06-22 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 22, 11, 11, 19, 82979, tzinfo=datetime.timezone.utc)),
        ),
    ]
