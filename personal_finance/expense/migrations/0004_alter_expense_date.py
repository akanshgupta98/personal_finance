# Generated by Django 5.0.6 on 2024-06-23 09:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_alter_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
    ]