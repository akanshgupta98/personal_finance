from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.api.views import (
    UserRegisteration,
    UserPasswordUpdate,
    UserPasswordReset,
    UserLogout,
)

urlpatterns = [
    path("register/", UserRegisteration.as_view(), name="registration"),
    path(
        "change-password/",
        UserPasswordUpdate.as_view(),
        name="updatepassword",
    ),
    path(
        "reset-password/",
        UserPasswordReset.as_view(),
        name="changepassword",
    ),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", UserLogout.as_view(), name="logout"),
]
