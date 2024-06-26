from django.db import models
from django.contrib.auth.models import User
from category.models import IncomeCategory
from personal_finance.model_manager import ModelManager

# Create your models here.


def get_income_model_manager_obj():
    """return IncomeModelManager object"""
    return IncomeModelManager()


class IncomeModelManager(ModelManager):
    """Model manager for Income Model"""

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(IncomeModelManager, cls).__new__(cls)

        return cls.instance

    def __init__(self):
        self.model = Income
        self.__obj = self.model.objects

    def get_model(self):
        return self.model

    def create(self, **data):
        """Create new instane of Income"""
        return self.__obj.create(**data)

    def fetch_all(self):
        """Fetch all instances of Income"""
        return self.__obj.all()

    def fetch_basis_pk(self, pk):
        """Fetch instance of Income based on pk"""
        return self.__obj.filter(pk=pk)


class Income(models.Model):
    """Model for storing income"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        name = str(self.amount) + "-" + str(self.source)
        return name
