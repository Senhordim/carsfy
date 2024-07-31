from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_filter = ('name',)
  search_fields = ('name',)
  ordering = ['name']
  fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    list_filter = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand', 'factory_year', 'model_year', 'value')
    ordering = ['model', 'brand', 'factory_year', 'model_year', 'value']
    fields = ('model', 'brand', 'factory_year', 'model_year', 'value', 'photo')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
