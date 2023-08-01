from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=190)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email

