from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('update_progress/', views.update_progress, name='update_progress'),
    path('track_progress/', views.track_progress, name='track_progress'),
]
