# serializers.py
from rest_framework import serializers
from .models import Choice  # Import the Choice model from your app's models.py

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
