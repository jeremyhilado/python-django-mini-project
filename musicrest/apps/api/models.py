from django.db import models
from apps.authentication.models import User


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name
