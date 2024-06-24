from expense.models import Expense
from personal_finance.model_manager import ModelManager


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


def get_model_manager_obj():
    """Function to return instance of ExpenseModelManager.

    Returns:
        Model Manager: ExpenseModelManager
    """
    return ExpenseModelManager()
