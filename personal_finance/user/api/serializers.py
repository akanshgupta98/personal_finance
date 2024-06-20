from rest_framework import serializers
from django.contrib.auth.models import User
from user.api.validators import Validators, EmailFieldValidator

from user import constants


class UserRegisterationSerializer(serializers.ModelSerializer):
    """
    Model Serializer for user registration
    """

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        """
        Meta class specifying meta data.
        """

        model = User
        fields = [
            constants.USER_FIRST_NAME,
            constants.USER_LAST_NAME,
            constants.USER_EMAIL,
            constants.USERNAME,
            constants.USER_PASSWORD,
            constants.USER_CONFIRM_PASSWORD,
        ]
        extra_kwargs = {
            constants.USER_PASSWORD: {constants.WRITE_ONLY_ARG: True},
        }

    def validate(self, attrs):
        """Validations for user data

        Args:
            attrs (dict): User data payload

        Returns:
            dict: validated data
        """

        validator = Validators()
        email_validator = EmailFieldValidator()

        # Password Validation
        validator.validate_fields_match(
            field_1=attrs.get(constants.USER_PASSWORD),
            field_2=attrs.get(constants.USER_CONFIRM_PASSWORD),
            err_msg=constants.PASSWORD_MISMATCH_ERR_MSG,
        )

        # blank field validation
        blank_validator_fields = [
            constants.USER_EMAIL,
            constants.USER_FIRST_NAME,
            constants.USER_LAST_NAME,
        ]

        for field in blank_validator_fields:
            validator.validate_field_blank(
                field=attrs.get(field),
                err_msg=constants.FIELD_BLANK_ERR_MSG.format(field),
            )

        # unique email validation

        email_validator.validate_email_unique(
            field=attrs.get(constants.USER_EMAIL),
            model=User,
            err_msg=constants.EMAIL_NOT_UNIQUE_ERR_MSG,
        )

        return attrs

    def create(self, validated_data):
        """Overrides create method of model serializer

        Args:
            validated_data (dict): validated user data

        Returns:
            Model: instance of User model
        """
        validated_data.pop(constants.USER_CONFIRM_PASSWORD)
        return User.objects.create_user(**validated_data)
