from django.db import models
from django.contrib.auth.models import User
from personal_finance.model_manager import ModelManager


def get_model_manager_obj():
    """Returns ExpenseCategoryModelManager object"""
    return ExpenseCategoryModelManager()


def get_income_model_manager_obj():
    """Returns IncomeCategoryModelManager object"""
    return IncomeCategoryModelManager()


class CategoryModelManager(ModelManager):
    """Base class for Managing category models"""

    def __init__(self, model_cls) -> None:
        """Initialize Category Model"""
        self.model = model_cls
        self.__obj = self.model.objects

    def get_model(self):
        """Returns Model"""
        return self.model

    def create(self, **kwargs):
        """Write data to Category Model

        Returns:
            Model: Category Model instance
        """
        return self.__obj.create(**kwargs)

    def list_data(self):
        """Get All data from Category model

        Returns:
            Model: Category Model instance
        """
        return self.__obj.all()

    def fetch_data_basis_pk(self, pk: str):
        """Get data based on Category model primary key

        Args:
            pk (str): primary key field name

        Returns:
            Model: Category Model instance
        """
        return self.__obj.filter(pk=pk)


class ExpenseCategoryModelManager(CategoryModelManager):
    """Class for managing ExpenseCategory Model"""

    def __init__(self):
        super().__init__(ExpenseCategory)


class IncomeCategoryModelManager(CategoryModelManager):
    """Class for managing IncomeCategory Model"""

    def __init__(self):
        super().__init__(IncomeCategory)


# Create your models here.
class ExpenseCategory(models.Model):
    """Model for Category. It will contain all expense categories"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, unique=True, null=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)


class IncomeCategory(models.Model):
    """Model for Income category"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)
