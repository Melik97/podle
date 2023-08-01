from django.db import models

from apis.models.customer import Customer
from apis.models.restaurant import Restaurant


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        null=False,
        default=1,
    )
    comment = models.TextField()

    def __str__(self):
        return self.customer.name

