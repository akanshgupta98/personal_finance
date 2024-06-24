from django.contrib import admin
from .models import get_model_manager_obj

# Register your models here.
model = get_model_manager_obj()
admin.site.register(model.get_model())
