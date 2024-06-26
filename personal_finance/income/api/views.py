from rest_framework import generics
from income.models import get_income_model_manager_obj
from income.api.serializers import ListIncomeSerializer, DetailIncomeSerializer


class ListIncome(generics.ListCreateAPIView):
    """Generic ListCreateAPIView view for add/get income"""

    queryset = get_income_model_manager_obj().fetch_all()
    serializer_class = ListIncomeSerializer


class DetailIncome(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic RetrieveUpdateDestroyAPIView view for
    add/get/delete income
    """

    queryset = get_income_model_manager_obj().get_model()
    serializer_class = DetailIncomeSerializer
