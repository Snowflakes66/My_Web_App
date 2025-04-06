from django.db import models

# Create your models here.
from django.db import models
from puzzles.models import Puzzle
from users.models import User

class Attempt(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    attempted_solution = models.CharField(max_length=100)
    result = models.BooleanField()  # correct/incorrect
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"Attempt {self.id} by {self.user.username}"

