
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    rating = models.IntegerField(default=1200)
    
    def __str__(self):
        return self.username