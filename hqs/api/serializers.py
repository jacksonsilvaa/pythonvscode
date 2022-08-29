from rest_framework import serializers
from hqs import models

class HqsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.hqs
        fields = '__all__'