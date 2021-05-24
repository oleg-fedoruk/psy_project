from rest_framework.serializers import ModelSerializer
from .models import SimpleTest


class SimpleTestSerializer(ModelSerializer):
    class Meta:
        model = SimpleTest
        fields = ['id', 'user', 'title', 'start_at', 'finished_at']
