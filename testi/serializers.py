from rest_framework import serializers

from .models import Product, Firm

class FirmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firm
        fields = ('id', 'name')