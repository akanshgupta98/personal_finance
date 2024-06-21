from rest_framework import generics
from django.contrib.auth.models import User
from user.api.serializers import (
    UserRegisterationSerializer,
    UserPasswordUpdateSerializer,
    UserPasswordResetSerializer,
)
from user.constants import USERNAME, USER_EMAIL
from django.shortcuts import get_object_or_404


class UserRegisteration(generics.CreateAPIView):
    """Generic CreateAPIView for user registration"""

    serializer_class = UserRegisterationSerializer


class UserPasswordUpdate(generics.UpdateAPIView):
    """Generic UpdateAPIView for user password update based on username"""

    serializer_class = UserPasswordUpdateSerializer
    lookup_field = USERNAME

    def get_queryset(self):
        username = self.kwargs["username"]
        return User.objects.filter(username=username)


class UserPasswordReset(generics.UpdateAPIView):
    serializer_class = UserPasswordResetSerializer

    def get_object(self):
        email = self.request.POST.get(USER_EMAIL)
        instance = get_object_or_404(User, email=email)
        return instance
