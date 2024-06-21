from django.urls import path
from user.api.views import UserRegisteration, UserPasswordUpdate, UserPasswordReset

urlpatterns = [
    path("register/", UserRegisteration.as_view(), name="registration"),
    # path("login/", admin.site.urls),
    # path("logout/", admin.site.urls),
    # path("recover-password/", admin.site.urls),
    path(
        "<str:username>/change-password/",
        UserPasswordUpdate.as_view(),
        name="updatepassword",
    ),
    path(
        "<str:email>/reset-password/",
        UserPasswordReset.as_view(),
        name="changepassword",
    ),
]
