from rest_framework import generics
from user.api.serializers import UserRegisterationSerializer


class UserRegisteration(generics.CreateAPIView):
    """Generic CreateAPIView for user registration"""

    serializer_class = UserRegisterationSerializer
