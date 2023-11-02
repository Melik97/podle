from django.contrib import admin

from .models.category import Category
from .models.customer import Customer
from .models.food import Food
from .models.menu import Menu
from .models.menu_restaurant import MenuRestaurant
from .models.reservation import Reservation
from .models.restaurant import Restaurant
from .models.review import Review


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'status']


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'restaurant']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Reservation)
admin.site.register(MenuRestaurant)
admin.site.register(Review)

