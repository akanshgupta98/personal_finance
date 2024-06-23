from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from expense.api.serializers import ListExpenseSerializer, DetailExpenseSerializer
from expense.models import ExpenseModelManager

from personal_finance.constants import PRIMARY_KEY


class ListExpense(generics.ListCreateAPIView):
    model_manager = ExpenseModelManager()
    queryset = model_manager.list_data()
    serializer_class = ListExpenseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DetailExpense(generics.RetrieveUpdateDestroyAPIView):
    model_manager = ExpenseModelManager()
    serializer_class = DetailExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs[PRIMARY_KEY]
        return self.model_manager.fetch_data_basis_pk(pk)
