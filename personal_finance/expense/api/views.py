from rest_framework import generics
from expense.api.serializers import ListExpenseSerializer, DetailExpenseSerializer
from expense.models import Expense
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ListExpense(generics.ListCreateAPIView):

    queryset = Expense.objects.all()
    serializer_class = ListExpenseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DetailExpense(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Expense.objects.filter(pk=pk)
