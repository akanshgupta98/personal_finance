"""Contains views for category app"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from category.api.serializers import (
    AddCategorySerializer,
    DetailCategorySerializer,
    AddIncomeCategorySerializer,
    DetailIncomeCategorySerializer,
)
from category.models import get_model_manager_obj, get_income_model_manager_obj
from personal_finance.constants import PRIMARY_KEY


class ListExpenseCategory(generics.ListCreateAPIView):
    """Generic ListCreateAPIView for list/add expense category"""

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = get_model_manager_obj().list_data()
    serializer_class = AddCategorySerializer


class DetailExpenseCategory(generics.RetrieveUpdateDestroyAPIView):
    """Generic RetrieveUpdateDestroyAPIView for individual expense category"""

    serializer_class = DetailCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get(PRIMARY_KEY)
        return get_model_manager_obj().fetch_data_basis_pk(pk)


class ListIncomeCategory(generics.ListCreateAPIView):
    """Generic ListCreateAPIView for list/add income category"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = get_income_model_manager_obj().list_data()

    serializer_class = AddIncomeCategorySerializer


class DetailIncomeCategory(generics.RetrieveUpdateDestroyAPIView):
    """Generic RetrieveUpdateDestroyAPIView for individual income category"""

    permission_classes = [IsAuthenticated]
    serializer_class = DetailIncomeCategorySerializer

    def get_queryset(self):
        pk = self.kwargs[PRIMARY_KEY]
        return get_income_model_manager_obj().fetch_data_basis_pk(pk)
