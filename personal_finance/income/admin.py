from django.contrib import admin
from income.models import get_income_model_manager_obj

# Register your models here.

model = get_income_model_manager_obj().get_model()
admin.site.register(model)
