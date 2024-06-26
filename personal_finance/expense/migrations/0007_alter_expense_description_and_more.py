# Generated by Django 5.0.6 on 2024-06-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0006_alter_expense_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='payment_method',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='reciept',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
