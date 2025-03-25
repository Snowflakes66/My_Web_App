from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Puzzle
from .serializers import PuzzleSerializer

class PuzzleListView(APIView):
    def get(self, request):
        puzzles = Puzzle.objects.all()
        serializer = PuzzleSerializer(puzzles, many=True)
        return Response(serializer.data)

