from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from category.api.serializers import (
    AddCategorySerializer,
    DetailCategorySerializer,
)
from category.models import get_model_manager_obj
from personal_finance.constants import *


class ListExpenseCategory(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = get_model_manager_obj().list_data()
    serializer_class = AddCategorySerializer


class DetailExpenseCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get(PRIMARY_KEY)
        return get_model_manager_obj().fetch_data_basis_pk(pk)
