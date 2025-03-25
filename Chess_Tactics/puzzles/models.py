from django.db import models
from users.models import User

class Puzzle(models.Model):
    difficulty_level = models.CharField(max_length=10)
    chess_position = models.CharField(max_length=100)  # FEN string
    solution = models.CharField(max_length=100)

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    attempted_solution = models.CharField(max_length=100)
    result = models.BooleanField()  # True if correct, False otherwise
