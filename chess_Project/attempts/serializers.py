from rest_framework import serializers
from .models import Attempt

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ['id', 'user', 'puzzle', 'solved', 'attempted_moves', 'timestamp']

class CreateAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ['puzzle', 'solved', 'attempted_moves']