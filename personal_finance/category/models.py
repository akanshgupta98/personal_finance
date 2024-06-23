from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ExpenseCategory(models.Model):
    """Model for Category. It will contain all expense categories"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, unique=True, null=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)
