from rest_framework.viewsets import ModelViewSet
from .models import SimpleTest
from .serializers import SimpleTestSerializer


class PsytestsViewSet(ModelViewSet):
    queryset = SimpleTest.objects.all()
    serializer_class = SimpleTestSerializer
