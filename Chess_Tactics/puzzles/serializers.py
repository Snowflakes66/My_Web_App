from rest_framework import serializers
from .models import Puzzle, Attempt

class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puzzle
        fields = ['id', 'difficulty_level', 'chess_position', 'solution']

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ['id', 'user', 'puzzle', 'attempted_solution', 'result']


