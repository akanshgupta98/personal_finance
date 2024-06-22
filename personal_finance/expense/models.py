from datetime import date
from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from django.utils import timezone

# Create your models here.


class Expense(models.Model):
    """Model for Expense. It will store all the expenses"""

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=100, null=True)
    payment_method = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    reciept = models.ImageField(null=True)
