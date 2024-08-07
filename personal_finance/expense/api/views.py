from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from expense.api.serializers import ListExpenseSerializer, DetailExpenseSerializer
from expense.model_manager import get_model_manager_obj

from personal_finance.constants import PRIMARY_KEY


class ListExpense(generics.ListCreateAPIView):
    model_manager = get_model_manager_obj()
    queryset = model_manager.list_data()
    serializer_class = ListExpenseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # pagination_class = PageNumberPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category"]
    search_fields = ["description"]
    ordering_fields = ["date"]


class DetailExpense(generics.RetrieveUpdateDestroyAPIView):
    model_manager = get_model_manager_obj()
    serializer_class = DetailExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs[PRIMARY_KEY]
        return self.model_manager.fetch_data_basis_pk(pk)
