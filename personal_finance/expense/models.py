from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from category.models import ExpenseCategory
from personal_finance.model_manager import ModelManager


# Create your models here.


class ExpenseModelManager(ModelManager):
    """A class to manage Expense Model operations"""

    def __init__(self) -> None:
        """Initialize Expense Model"""
        self.model = Expense
        self.__obj = self.model.objects

    def get_model(self):
        return self.model

    def create(self, **kwargs):
        """Write data to Expense Model

        Returns:
            Model: Expense Model instance
        """
        return self.__obj.create(**kwargs)

    def list_data(self):
        """Get All data from Expense model

        Returns:
            Model: Expense Model instance
        """
        return self.__obj.all()

    def fetch_data_basis_pk(self, pk: str):
        """Get data based on Expense model primary key

        Args:
            pk (str): primary key field name

        Returns:
            Model: Expense Model instance
        """
        return self.__obj.filter(pk=pk)


class Expense(models.Model):
    """Model for Expense. It will store all the expenses"""

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(default=timezone.localdate)
    description = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(to=ExpenseCategory, on_delete=models.CASCADE)
    reciept = models.ImageField(null=True, blank=True)

    def __str__(self):
        name = str(self.amount) + "-" + str(self.category)
        return name
