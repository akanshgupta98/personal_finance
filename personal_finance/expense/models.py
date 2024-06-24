from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from category.models import get_model_manager_obj


# Create your models here.


class Expense(models.Model):
    """Model for Expense. It will store all the expenses"""

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(default=timezone.localdate)
    description = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(
        to=get_model_manager_obj().get_model(), on_delete=models.CASCADE
    )
    reciept = models.ImageField(null=True, blank=True)

    def __str__(self):
        name = str(self.amount) + "-" + str(self.category)
        return name
