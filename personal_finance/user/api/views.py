from rest_framework import generics
from django.contrib.auth.models import User
from user.api.serializers import (
    UserRegisterationSerializer,
    UserPasswordUpdateSerializer,
    UserPasswordResetSerializer,
)
from user.constants import USERNAME, USER_EMAIL


class UserRegisteration(generics.CreateAPIView):
    """Generic CreateAPIView for user registration"""

    serializer_class = UserRegisterationSerializer


class UserPasswordUpdate(generics.UpdateAPIView):
    """Generic UpdateAPIView for user password update based on username"""

    queryset = User.objects.all()
    serializer_class = UserPasswordUpdateSerializer
    lookup_field = USERNAME


class UserPasswordReset(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordResetSerializer
    lookup_field = USER_EMAIL
