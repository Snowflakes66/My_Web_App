from django.urls import path
from .views import PuzzleListView

urlpatterns = [
    path('puzzles/', PuzzleListView.as_view()),
    
]
