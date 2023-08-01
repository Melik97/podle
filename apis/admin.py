from django.contrib import admin

from .models.menu import Menu
from .models.restaurant import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'status']

class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'status', 'restaurant_id']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)

