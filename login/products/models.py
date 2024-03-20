from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/images/')
    date = models.DateField(default=timezone.now, null=True)

    def __str__(self):
        return self.name


