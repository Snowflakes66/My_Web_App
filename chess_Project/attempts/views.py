from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Attempt
from .serializers import AttemptSerializer, CreateAttemptSerializer
from rest_framework.permissions import IsAuthenticated

class AttemptList(generics.ListAPIView):
    serializer_class = AttemptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Attempt.objects.filter(user=self.request.user)

class CreateAttempt(generics.CreateAPIView):
    serializer_class = CreateAttemptSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)