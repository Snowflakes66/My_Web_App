from django.urls import path
from .views import PuzzleList, PuzzleDetail, RandomPuzzle
from. import views


urlpatterns = [
    path('', PuzzleList.as_view()),
    path('<int:pk>/', PuzzleDetail.as_view()),
    path('random/', RandomPuzzle.as_view()),
]