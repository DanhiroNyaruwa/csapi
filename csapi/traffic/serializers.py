from rest_framework import serializers
from .models import AADF


class AADFSerializer(serializers.ModelSerializer):
    class Meta:
        model = AADF
        fields = '__all__'
