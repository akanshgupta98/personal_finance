CATEGORY_NAME = "name"
ERROR = "error"
USER_PASSWORD = "password"
USER_FIRST_NAME = "first_name"
USER_LAST_NAME = "first_name"
USER_CONFIRM_PASSWORD = "confirm_password"
USER_EMAIL = "email"
USERNAME = "username"
WRITE_ONLY_ARG = "write_only"
READ_ONLY_ARG = "read_only"
USER_OLD_PASSWORD = "old_password"
USER_NEW_PASSWORD = "new_password"
TOKEN = "token"
USER_FIELD = "user"
ALL_MODEL_FIELDS = "__all__"
REQUEST_DATA = "request"

INPUT_TYPE_ARG = "input_type"
STYLE_ARG = "style"


"""ERROR MESSAGES"""
DEFAULT_VALIDATION_FAILURE_ERR_MSG = "Validation for fields failed"
MISMATCH_ERR_MSG = "{} and {} fields do not match. "
MATCH_ERR_MSG = "{} and {} cannot be same"
EMAIL_NOT_UNIQUE_ERR_MSG = (
    "A user with same email already exists.Try to login, or change password."
)
FIELD_BLANK_ERR_MSG = "This field: {} is required. Empty value not allowed "
INCORRECT_USER_PASSWORD = "Incorrect password entered for the user"
CATEGORY_NAME_SAME_VALUE_ERR_MSG = (
    "Existing value and new value for category cannot be same"
)
PRIMARY_KEY = "pk"
