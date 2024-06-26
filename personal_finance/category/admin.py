from django.contrib import admin
from .models import get_model_manager_obj, get_income_model_manager_obj

# Register your models here.
model = get_model_manager_obj().get_model()
admin.site.register(model)
model = get_income_model_manager_obj().get_model()
admin.site.register(model)
