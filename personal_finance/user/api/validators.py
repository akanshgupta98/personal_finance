""" 
Module for validating user input
"""

from rest_framework import serializers
from user.constants import *


class Validators:
    """
    A utility class for validating fields.
    """

    def __init__(self):
        """
        Initializes data
        """
        self.default_err_msg = DEFAULT_VALIDATION_FAILURE_ERR_MSG
        self.err_dict = {ERROR: self.default_err_msg}

    def _validation_error(self, err_msg):

        if err_msg is not None:
            self.err_dict[ERROR] = err_msg

        return serializers.ValidationError(self.err_dict)

    def validate_fields_match(self, field_1, field_2, err_msg=None):
        """Validate two fields match

        Args:
            field_1 : field to be validated
            field_2 : field to be validated
            err_msg (optional): err msg to be raised. Defaults to None.

        Raises:
            Validation Error: If two fields do not match
        """

        if field_1 != field_2:
            raise self._validation_error(err_msg)

    def validate_field_blank(self, field, err_msg=None):
        """Validate blank field

        Args:
            field (str): field to be validated
            err_msg (str, optional): msg to be raised in exception. Defaults to None.

        Raises:
            Validation Error: If field is blank
        """
        if len(field) == 0:
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
        if model.objects.filter(email=field).exists():
            raise self._validation_error(err_msg)
