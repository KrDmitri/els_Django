from rest_framework import serializers
from .models import ELS_PRODUCT

class ELSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ELS_PRODUCT
        fields = ['name', 'value']
