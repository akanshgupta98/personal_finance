ERROR = "error"
USER_PASSWORD = "password"
USER_FIRST_NAME = "first_name"
USER_LAST_NAME = "first_name"
USER_CONFIRM_PASSWORD = "confirm_password"
USER_EMAIL = "email"
USERNAME = "username"
WRITE_ONLY_ARG = "write_only"


"""ERROR MESSAGES"""
DEFAULT_VALIDATION_FAILURE_ERR_MSG = "Validation for fields failed"
PASSWORD_MISMATCH_ERR_MSG = "Password and confirm_password fields do not match. "
EMAIL_NOT_UNIQUE_ERR_MSG = (
    "A user with same email already exists.Try to login, or change password."
)
FIELD_BLANK_ERR_MSG = "Empty field: {} value not allowed "
