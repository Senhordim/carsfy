from django.contrib import admin
from cars.models import Car

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    list_filter = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand', 'factory_year', 'model_year', 'value')
    ordering = ['model', 'brand', 'factory_year', 'model_year', 'value']
    fields = ('model', 'brand', 'factory_year', 'model_year', 'value')

admin.site.register(Car, CarAdmin)
