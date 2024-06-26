from rest_framework import serializers
from income.models import get_income_model_manager_obj
from personal_finance.constants import *
from personal_finance.loging import get_logger


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_income_model_manager_obj().get_model()
        fields = ALL_MODEL_FIELDS
        extra_kwargs = {USER_FIELD: {READ_ONLY_ARG: True}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_manager = get_income_model_manager_obj()
        self.logger = get_logger(__name__)


class ListIncomeSerializer(IncomeSerializer):

    def create(self, validated_data):
        self.logger.Info(f"New income add request called with {validated_data}")
        validated_data[USER_FIELD] = self._context[REQUEST_DATA].user
        ins = self.model_manager.create(**validated_data)
        self.logger.Info("New income entry added successfully")
        return ins


class DetailIncomeSerializer(IncomeSerializer):
    pass
