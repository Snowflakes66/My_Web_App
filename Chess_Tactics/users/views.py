

# Create your views here.



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Progress

@login_required
def update_progress(request):
    progress, created = Progress.objects.get_or_create(user=request.user)
    if created:
        progress.save()
    return redirect('profile')

@login_required
def track_progress(request):
    progress, created = Progress.objects.get_or_create(user=request.user)
    attempts = Attempt.objects.filter(user=request.user)
    puzzles_solved = attempts.filter(result=True).count()
    puzzles_attempted = attempts.count()
    accuracy = (puzzles_solved / puzzles_attempted) * 100 if puzzles_attempted > 0 else 0
    progress.puzzles_solved = puzzles_solved
    progress.puzzles_attempted = puzzles_attempted
    progress.accuracy = accuracy
    progress.save()
    return redirect('profile')
