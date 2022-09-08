from rest_framework.serializers import ModelSerializer
from .models import Choice

class ChoicesSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'