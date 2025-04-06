from django.db import models
from users.models import User

class Puzzle(models.Model):
    id = models.AutoField(primary_key=True)
    difficulty_level = models.CharField(max_length=10)
    chess_position = models.CharField(max_length=100)  # FEN string
    solution = models.CharField(max_length=100)

    def __str__(self):
        return f"Puzzle {self.id} - {self.difficulty_level}"

