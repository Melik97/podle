from django.db import models

from apis.models.menu import Menu
from apis.models.restaurant import Restaurant


class MenuRestaurant(models.Model):
    restaurant_id = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        null=False
    )
    menu_id = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        null=False
    )

    class Meta:
        db_table = 'menu_restaurant'


