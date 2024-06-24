from django.contrib import admin
from .model_manager import get_model_manager_obj

# Register your models here.
model = get_model_manager_obj()
admin.site.register(model.get_model())
