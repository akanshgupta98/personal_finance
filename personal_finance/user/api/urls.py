from django.urls import path
from user.api.views import UserRegisteration

urlpatterns = [
    path("register/", UserRegisteration.as_view(), name="registration"),
    # path("login/", admin.site.urls),
    # path("logout/", admin.site.urls),
    # path("recover-password/", admin.site.urls),
    # path("reset-password/", admin.site.urls),
]
