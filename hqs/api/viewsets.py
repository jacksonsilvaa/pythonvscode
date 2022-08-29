from rest_framework import viewsets
from hqs.api import serializers
from hqs import models

class HqsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HqsSerializers
    queryset = models.hqs.objects.all()