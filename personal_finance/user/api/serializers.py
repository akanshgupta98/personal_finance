from rest_framework import serializers
from django.contrib.auth.models import User
from user.api.validators import UserAPIValidator

from personal_finance.constants import *


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
            USER_FIRST_NAME,
            USER_LAST_NAME,
            USER_EMAIL,
            USERNAME,
            USER_PASSWORD,
            USER_CONFIRM_PASSWORD,
        ]
        extra_kwargs = {
            USER_PASSWORD: {WRITE_ONLY_ARG: True},
        }

    def validate(self, attrs):
        """Validations for user data

        Args:
            attrs (dict): User data payload

        Returns:
            dict: validated data
        """

        # validator = Validators(attrs)
        user_api_validator = UserAPIValidator(attrs)

        # Password Validation
        user_api_validator.validate_fields_match(USER_PASSWORD, USER_CONFIRM_PASSWORD)

        # blank field validation
        blank_validator_fields = [
            USER_EMAIL,
            USER_FIRST_NAME,
            USER_LAST_NAME,
        ]

        for field in blank_validator_fields:
            user_api_validator.validate_field_not_blank(field)

        # unique email validation

        user_api_validator.validate_email_unique(
            field=USER_EMAIL,
            model=User,
            err_msg=EMAIL_NOT_UNIQUE_ERR_MSG,
        )

        return attrs

    def create(self, validated_data):
        """Overrides create method of model serializer

        Args:
            validated_data (dict): validated user data

        Returns:
            Model: instance of User model
        """
        validated_data.pop(USER_CONFIRM_PASSWORD)
        return User.objects.create_user(**validated_data)


class UserPasswordUpdateSerializer(serializers.ModelSerializer):
    """Model serializer for user password update"""

    old_password = serializers.CharField(
        style={INPUT_TYPE_ARG: USER_PASSWORD}, write_only=True
    )
    new_password = serializers.CharField(
        style={INPUT_TYPE_ARG: USER_PASSWORD}, write_only=True
    )
    confirm_password = serializers.CharField(
        style={INPUT_TYPE_ARG: USER_PASSWORD}, write_only=True
    )

    class Meta:
        """Meta data for model serializer"""

        model = User
        fields = [
            USER_OLD_PASSWORD,
            USER_NEW_PASSWORD,
            USER_CONFIRM_PASSWORD,
        ]

    def validate(self, attrs):

        data_validator = UserAPIValidator(attrs)

        data_validator.validate_fields_match(USER_NEW_PASSWORD, USER_CONFIRM_PASSWORD)

        data_validator.validate_fields_not_match(USER_OLD_PASSWORD, USER_NEW_PASSWORD)

        return attrs

    def update(self, instance, validated_data):
        if instance.check_password(validated_data[USER_OLD_PASSWORD]):
            instance.set_password(validated_data[USER_NEW_PASSWORD])
            instance.save()
        else:
            raise serializers.ValidationError({ERROR: INCORRECT_USER_PASSWORD})

        return instance


class UserPasswordResetSerializer(serializers.ModelSerializer):
    """Model serializer for user password reset functionality."""

    class Meta:
        """Meta data for Model serializer"""

        model = User
        fields = [USER_EMAIL, USER_PASSWORD]
        extra_kwargs = {
            USER_PASSWORD: {
                STYLE_ARG: {INPUT_TYPE_ARG: USER_PASSWORD},
                WRITE_ONLY_ARG: True,
            }
        }

    def validate(self, attrs):

        data_validator = UserAPIValidator(attrs)
        blank_fields = [USER_EMAIL, USER_PASSWORD]
        for field in blank_fields:
            data_validator.validate_field_not_blank(field)

        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data[USER_PASSWORD])
        instance.save()
        return instance
