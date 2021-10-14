from rest_framework import serializers
from nogcodevapp.models.usuario import User
from nogcodevapp.models.factura import Factura
from nogcodevapp.serializers.facturaSerializer import FacturaSerializer


class UserSerializer(serializers.ModelSerializer):
    factura = FacturaSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']

    def create(self, validated_data):
        facturaData = validated_data.pop('factura')
        userInstance = User.objects.create(**validated_data)
        Factura.objects.create(user=userInstance, **facturaData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        factura = Factura.objects.get(user=obj.id)
        return {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email,
                'account': {
                    'id': factura.id,
                    'user': factura.user,
                    'Date': factura.fecha,
            }
        }

