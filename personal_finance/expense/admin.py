from django.contrib import admin
from .models import ExpenseModelManager

# Register your models here.
admin.site.register(ExpenseModelManager().get_model())
