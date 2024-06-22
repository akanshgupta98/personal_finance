from django.urls import path
from category.api.views import ListCategory, DetailCategory

urlpatterns = [
    path("list/", ListCategory.as_view(), name="add-category"),
    path("detail/<int:pk>", DetailCategory.as_view(), name="detail"),
]
