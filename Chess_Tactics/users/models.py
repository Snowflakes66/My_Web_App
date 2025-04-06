

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)



class Progress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puzzles_solved = models.IntegerField(default=0)
    puzzles_attempted = models.IntegerField(default=0)
    accuracy = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Progress"