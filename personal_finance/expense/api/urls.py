from django.urls import path
from expense.api.views import ListExpense, DetailExpense

urlpatterns = [
    path("list/", ListExpense.as_view(), name="list-expenses"),
    path("detail/<int:pk>", DetailExpense.as_view(), name="detail-expense"),
]
