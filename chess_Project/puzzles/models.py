
# Create your models here.
from django.db import models

class Puzzle(models.Model):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    EXPERT = 4
    
    DIFFICULTY_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
        (EXPERT, 'Expert'),
    ]
    
    fen = models.CharField(max_length=100)
    moves = models.JSONField()
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES)
    rating = models.IntegerField(default=1200)

    def __str__(self):
        return f"Puzzle {self.id} - {self.get_difficulty_display()}"