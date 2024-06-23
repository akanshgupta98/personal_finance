from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from category.api.serializers import (
    AddCategorySerializer,
    DetailCategorySerializer,
)
from category.models import ExpenseCategory
from personal_finance.constants import *


class ListCategory(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = ExpenseCategory.objects.all()
    serializer_class = AddCategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get(PRIMARY_KEY)
        return ExpenseCategory.objects.filter(pk=pk)
