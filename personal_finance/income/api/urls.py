from django.urls import path
from income.api.views import ListIncome, DetailIncome

urlpatterns = [
    path("list-income/", ListIncome.as_view(), name="list-income"),
    path("detail-income/<int:pk>", DetailIncome.as_view(), name="detail-income"),
]
