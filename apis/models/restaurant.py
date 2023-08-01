from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=190)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurant/profiles/')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

