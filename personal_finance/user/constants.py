ERROR = "error"
USER_PASSWORD = "password"
USER_FIRST_NAME = "first_name"
USER_LAST_NAME = "first_name"
USER_CONFIRM_PASSWORD = "confirm_password"
USER_EMAIL = "email"
USERNAME = "username"
WRITE_ONLY_ARG = "write_only"
USER_OLD_PASSWORD = "old_password"
USER_NEW_PASSWORD = "new_password"

INPUT_TYPE_ARG = "input_type"


"""ERROR MESSAGES"""
DEFAULT_VALIDATION_FAILURE_ERR_MSG = "Validation for fields failed"
MISMATCH_ERR_MSG = "{} and {} fields do not match. "
MATCH_ERR_MSG = "{} and {} cannot be same"
EMAIL_NOT_UNIQUE_ERR_MSG = (
    "A user with same email already exists.Try to login, or change password."
)
FIELD_BLANK_ERR_MSG = "Empty field: {} value not allowed "
INCORRECT_USER_PASSWORD = "Incorrect password entered for the user"
