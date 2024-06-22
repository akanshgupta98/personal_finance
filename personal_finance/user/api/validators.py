""" 
Module for validating user input
"""

from personal_finance.constants import *
from personal_finance.validators import Validators


class UserAPIValidator(Validators):
    """User API Validator Class."""

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
