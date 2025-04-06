from django.urls import path
from .views import AttemptList, CreateAttempt

urlpatterns = [
    path('', AttemptList.as_view()),
    path('create/', CreateAttempt.as_view()),
]