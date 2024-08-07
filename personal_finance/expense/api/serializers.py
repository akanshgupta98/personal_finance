from rest_framework import serializers
from expense.model_manager import get_model_manager_obj
from personal_finance.constants import *
from personal_finance.loging import Logger


class ExpenseSerializer(serializers.ModelSerializer):
    """Base class for Expense Serializer"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = Logger(__name__)
        self.model_manager = get_model_manager_obj()

    class Meta:
        """Meta data for Expense Serializer"""

        model = get_model_manager_obj().get_model()
        fields = ALL_MODEL_FIELDS
        extra_kwargs = {USER_FIELD: {READ_ONLY_ARG: True}}


class ListExpenseSerializer(ExpenseSerializer):
    """Model serializer for ListExpense View. Inherits ExpenseSerializer"""

    def create(self, validated_data):
        self.logger.Info(f"Expense serializer create called with data:{validated_data}")

        user = self._context[REQUEST_DATA].user
        self.logger.Debug(f"User creating this expense is {user}")
        validated_data[USER_FIELD] = user
        expense = self.model_manager.create(**validated_data)

        self.logger.Info("New Expense entry created successfully")
        return expense


class DetailExpenseSerializer(ExpenseSerializer):
    """Model serializer for DetailExpense View. Inherits ExpenseSerializer"""

    # user = serializers.CharField(source="user.username")
    # category = serializers.CharField(source="category.name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = Logger(__name__)
