from rest_framework import serializers
from category.models import get_model_manager_obj
from personal_finance.constants import *
from category.api.validators import CategoryAPIValidator
from personal_finance.loging import Logger


class CategorySerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.logger = Logger(__name__)
        self.model_manager = get_model_manager_obj()


class AddCategorySerializer(CategorySerializer):
    """Model serializer for adding/ listing categories"""

    class Meta:
        """Meta data for Model serializer"""

        model = get_model_manager_obj().get_model()
        fields = ALL_MODEL_FIELDS
        extra_kwargs = {USER_FIELD: {READ_ONLY_ARG: True}}

    def create(self, validated_data):

        self.logger.Debug("Add category create called")
        validated_data[USER_FIELD] = self._context[REQUEST_DATA].user
        return self.model_manager.create(**validated_data)


class DetailCategorySerializer(CategorySerializer):
    """Model serializer for single category"""

    name = serializers.CharField()

    class Meta:
        """Meta data for model serializer"""

        model = get_model_manager_obj().get_model()
        fields = [CATEGORY_NAME, USER_FIELD]
        extra_kwargs = {USER_FIELD: {READ_ONLY_ARG: True}}

    def validate(self, attrs):
        category_validator = CategoryAPIValidator(attrs)
        category_validator.validate_no_duplicate_update(CATEGORY_NAME)
        return attrs
