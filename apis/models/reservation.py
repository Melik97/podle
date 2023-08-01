from django.db import models

from apis.models.customer import Customer
from apis.models.restaurant import Restaurant


class Reservation(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )
    reservation_time = models.DateTimeField()
    num_guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.customer.name} - {self.restaurant.name}"

