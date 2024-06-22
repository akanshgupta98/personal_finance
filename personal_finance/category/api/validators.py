from personal_finance.validators import Validators
from category.models import Category
from personal_finance.constants import *
from rest_framework import serializers


class CategoryAPIValidator(Validators):
    """Validator for category API"""

    def __init__(self, attrs):
        self.model = Category
        super().__init__(attrs)

    def validate_no_duplicate_update(self, field: str):
        """
        Validates that the new value does not match the existing value
        in the database.

        Args:
            field (str): field to be validated

        Raises:
            Validation Error: If the new value matches the existing value.
        """
        self._get_data(field)
        old_name = self.model.objects.get(name=self.fields[0])
        if old_name.name == self.fields[0]:
            raise self._validation_error(err_msg=CATEGORY_NAME_SAME_VALUE_ERR_MSG)
