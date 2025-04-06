from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Puzzle
from .serializers import PuzzleSerializer
from rest_framework.permissions import IsAuthenticated

class PuzzleList(generics.ListAPIView):
    queryset = Puzzle.objects.all()
    serializer_class = PuzzleSerializer
    # permission_classes = [IsAuthenticated]

class PuzzleDetail(generics.RetrieveAPIView):
    queryset = Puzzle.objects.all()
    serializer_class = PuzzleSerializer
    permission_classes = [IsAuthenticated]

class RandomPuzzle(generics.RetrieveAPIView):
    queryset = Puzzle.objects.all()
    serializer_class = PuzzleSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        difficulty = self.request.query_params.get('difficulty', None)
        if difficulty:
            return Puzzle.objects.filter(difficulty=difficulty).order_by('?').first()
        return Puzzle.objects.order_by('?').first()



def puzzle_list(request):
    puzzles = Puzzle.objects.all()
    return render(request, 'puzzles/puzzle_list.html', {'puzzles': puzzles})

