from rest_framework import serializers
from expense.models import ExpenseModelManager
from personal_finance.constants import *
from personal_finance.loging import Logger


class ListExpenseSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = Logger(__name__)
        self.model_manager = ExpenseModelManager()

    class Meta:
        model = ExpenseModelManager().get_model()
        fields = ALL_MODEL_FIELDS
        extra_kwargs = {USER_FIELD: {READ_ONLY_ARG: True}}

    def create(self, validated_data):
        self.logger.Info(f"Expense serializer create called with data:{validated_data}")

        user = self._context[REQUEST_DATA].user
        self.logger.Debug(f"User creating this expense is {user}")
        validated_data[USER_FIELD] = user
        new_user = self.model_manager.create(**validated_data)

        self.logger.Info("New Expense entry created successfully")
        return new_user


class DetailExpenseSerializer(serializers.ModelSerializer):

    # user = serializers.CharField(source="user.username")
    # category = serializers.CharField(source="category.name")

    class Meta:

        model = ExpenseModelManager().get_model()
        fields = ALL_MODEL_FIELDS
        extra_kwargs = {USER_FIELD: {READ_ONLY_ARG: True}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = Logger(__name__)
