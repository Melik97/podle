from django.db import models
from django.db.models import CASCADE

from apis.models.restaurant import Restaurant


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(
        upload_to='restaurant/menus/',
        blank=True,
        null=True
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    restaurant_id = models.ForeignKey(
        Restaurant,
        on_delete=CASCADE,
        db_constraint=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

