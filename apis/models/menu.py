from django.db import models
from apis.models.category import Category
from apis.models.restaurant import Restaurant


class Menu(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        null=False,
        default=False,
    )

    def __str__(self):
        if self.category.name:
            return self.category.name
        return self.name

    class Meta:
        ordering = ['-id']

