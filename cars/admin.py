from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import escape
from cars.models import Car, Brand

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_filter = ('name',)
  search_fields = ('name',)
  ordering = ['name']
  fields = ('name',)


class CarAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
      return format_html('<img src="%s" width="100" height="60" />' % escape(obj.photo.url))

    image_tag.short_description = 'Image'

    list_display = ('image_tag', 'model', 'brand', 'model_year', 'value', 'created_at')
    list_filter = ('model', 'brand', 'model_year', 'value')
    search_fields = ('model', 'brand', 'factory_year', 'model_year', 'value')
    ordering = ['model', 'brand', 'factory_year', 'model_year', 'value']
    fields = ('model', 'brand', 'factory_year', 'model_year', 'value', 'plate', 'photo')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
