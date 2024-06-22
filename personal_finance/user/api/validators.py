""" 
Module for validating user input
"""

from rest_framework import serializers
from user.constants import *


class Validators:
    """
    A utility class for validating fields.
    """

    def __init__(self, attrs):
        """
        Initializes data
        """
        self.data = attrs
        self.default_err_msg = DEFAULT_VALIDATION_FAILURE_ERR_MSG
        self.err_dict = {ERROR: self.default_err_msg}
        self.fields = []

    def _get_data(self, *argv):
        self.fields.clear()
        for arg in argv:
            self.fields.append(self.data.get(arg))

        print("fields data is: ", self.fields)

    def _validation_error(self, err_msg):

        if err_msg is not None:
            self.err_dict[ERROR] = err_msg
        else:
            self.err_dict[ERROR] = self.default_err_msg

        return serializers.ValidationError(self.err_dict)

    def validate_fields_match(self, field_1, field_2, err_msg=None):
        """Validate two fields match

        Args:
            field_1 (str): field to be validated
            field_2 (str): field to be validated
            err_msg (optional): err msg to be raised. Defaults to None.

        Raises:
            Validation Error: If two fields do not match
        """
        self._get_data(field_1, field_2)
        self.default_err_msg = MISMATCH_ERR_MSG.format(field_1, field_2)

        # raise error if all elements in fields are not same.
        if len(set(self.fields)) != 1:
            raise self._validation_error(err_msg)

    def validate_field_not_blank(self, field, err_msg=None):
        """Validate blank field

        Args:
            field (str): field to be validated
            err_msg (str, optional): msg to be raised in exception. Defaults to None.

        Raises:
            Validation Error: If field is blank
        """
        print(f"{__class__.__name__}")
        self.default_err_msg = FIELD_BLANK_ERR_MSG.format(field)
        self._get_data(field)

        # Raise validation error if any field is blank
        for field_val in self.fields:
            if field_val is None or len(field_val) == 0:
                raise self._validation_error(err_msg)

    def validate_fields_not_match(self, field_1: str, field_2: str, err_msg=None):
        """Validate uniqueness of fields

        Args:
            field_1 (str): field to be validated
            field_2 (str): field to be validated
            err_msg (str, optional): msg to be raised in exception. Defaults to None.

        Raises:
            Validation Error: If fields are same
        """

        self._get_data(field_1, field_2)

        self.default_err_msg = MATCH_ERR_MSG.format(field_1, field_2)

        # raise validation error if all fields are match
        if len(set(self.fields)) == 1:
            raise self._validation_error(err_msg)


class EmailFieldValidator(Validators):
    """Email Validator Class."""

    def validate_email_unique(self, model, field, err_msg=None):
        """Validate Unique email address

        Args:
            model (Model): Model in which email should be checked
            field (str): field to be validated
            err_msg (str, optional): msg to be raised in exception. Defaults to None.

        Raises:
            Validation Error: If email is not unique
        """
        self._get_data(field)

        if model.objects.filter(email=self.fields[0]).exists():
            raise self._validation_error(err_msg)
