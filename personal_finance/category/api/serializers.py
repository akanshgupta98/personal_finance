from rest_framework import serializers
from category.models import ExpenseCategory
from personal_finance.constants import *
from category.api.validators import CategoryAPIValidator
from personal_finance.loging import Logger


class AddCategorySerializer(serializers.ModelSerializer):
    """Model serializer for adding/ listing categories"""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.logger = Logger(__name__)

    class Meta:
        """Meta data for Model serializer"""

        model = ExpenseCategory
        fields = ALL_MODEL_FIELDS
        extra_kwargs = {USER_FIELD: {READ_ONLY_ARG: True}}

    def create(self, validated_data):

        self.logger.Debug("Add category create called")
        validated_data[USER_FIELD] = self._context[REQUEST_DATA].user
        return ExpenseCategory.objects.create(**validated_data)


class DetailCategorySerializer(serializers.ModelSerializer):
    """Model serializer for single category"""

    name = serializers.CharField()

    class Meta:
        """Meta data for model serializer"""

        model = ExpenseCategory
        fields = [CATEGORY_NAME, USER_FIELD]
        extra_kwargs = {USER_FIELD: {READ_ONLY_ARG: True}}

    def validate(self, attrs):
        category_validator = CategoryAPIValidator(attrs)
        category_validator.validate_no_duplicate_update(CATEGORY_NAME)
        return attrs
