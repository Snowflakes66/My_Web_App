

# Create your views here.

from django.shortcuts import render, redirect
from .models import Attempt
from users.views import track_progress

def attempt_view(request):
    # ...
    attempt.save()
    track_progress(request)
    return redirect('profile')
