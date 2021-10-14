from nogcodevapp.models.factura import Factura
from rest_framework import serializers


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['user', 'fecha']