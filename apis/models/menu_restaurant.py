from django.db import models

from apis.models.menu import Menu
from apis.models.restaurant import Restaurant


class MenuRestaurant(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        null=False
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        null=False
    )

