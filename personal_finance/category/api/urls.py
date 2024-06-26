from django.urls import path
from category.api.views import (
    ListExpenseCategory,
    DetailExpenseCategory,
    ListIncomeCategory,
    DetailIncomeCategory,
)

urlpatterns = [
    path("list-expense/", ListExpenseCategory.as_view(), name="add-category"),
    path("detail-expense/<int:pk>", DetailExpenseCategory.as_view(), name="detail"),
    path("list-income/", ListIncomeCategory.as_view(), name="add-category"),
    path("detail-income/<int:pk>", DetailIncomeCategory.as_view(), name="detail"),
]
