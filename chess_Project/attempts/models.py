from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from puzzles.models import Puzzle

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    solved = models.BooleanField()
    attempted_moves = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s attempt on Puzzle {self.puzzle.id}"