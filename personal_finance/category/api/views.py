from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from category.api.serializers import (
    AddCategorySerializer,
    DetailCategorySerializer,
)
from category.models import Category


class ListCategory(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all()
    serializer_class = AddCategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Category.objects.filter(pk=pk)
