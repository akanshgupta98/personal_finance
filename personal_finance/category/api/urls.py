from django.urls import path
from category.api.views import ListExpenseCategory, DetailExpenseCategory

urlpatterns = [
    path("list/", ListExpenseCategory.as_view(), name="add-category"),
    path("detail/<int:pk>", DetailExpenseCategory.as_view(), name="detail"),
]
