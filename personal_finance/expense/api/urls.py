from django.urls import path
from expense.api.views import ListExpense, DetailExpense

urlpatterns = [
    path("", ListExpense.as_view(), name="list-expenses"),
    path("/<int:pk>", DetailExpense.as_view(), name="detail-expense"),
]
