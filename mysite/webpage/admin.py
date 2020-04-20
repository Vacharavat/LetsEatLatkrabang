from django.contrib import admin
from webpage.models import restaurant, restaurant_type

# Register your models here.
class restaurant_info(admin.ModelAdmin):
    list_display = ['id', 'restaurant_name', 'desc', 'picture']
    list_filter = ['restaurant_name']
    search_fields = ['restaurant_name']
admin.site.register(restaurant, restaurant_info)
admin.site.register(restaurant_type)