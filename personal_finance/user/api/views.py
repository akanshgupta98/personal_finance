from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from user.api.serializers import (
    UserRegisterationSerializer,
    UserPasswordUpdateSerializer,
    UserPasswordResetSerializer,
)
from personal_finance.constants import USERNAME, USER_EMAIL


class UserRegisteration(generics.CreateAPIView):
    """Generic CreateAPIView for user registration"""

    serializer_class = UserRegisterationSerializer


class UserPasswordUpdate(generics.UpdateAPIView):
    """Generic UpdateAPIView for user password update based on username"""

    serializer_class = UserPasswordUpdateSerializer
    lookup_field = USERNAME

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs["username"]
        return User.objects.filter(username=username)


class UserPasswordReset(generics.UpdateAPIView):
    """Generic UpdateAPIView for User password reset."""

    serializer_class = UserPasswordResetSerializer

    def get_object(self):
        email = self.request.POST.get(USER_EMAIL)
        instance = get_object_or_404(User, email=email)
        return instance


class UserLogout(generics.CreateAPIView):
    """Generic CreateAPIView for user log out."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"detail": "User logged out successfully"})
