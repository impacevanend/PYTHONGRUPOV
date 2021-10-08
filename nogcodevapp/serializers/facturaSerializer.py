from rest_framework import serializers
from nogcodevapp.models.usuario import User
from nogcodevapp.models.factura import Factura
from nogcodevapp.serializers.usuarioSerializer import UsuarioSerializer


class FacturaSerializer(serializers.ModelSerializer):
    account = UsuarioSerializer()
    class Meta:
        model = Factura
        fields = ['fecha']
        
        
    def create(self, validated_data):
        userData = validated_data.pop('account')
        facturaInstance = User.objects.create(**validated_data)
        User.objects.create(factura=facturaInstance, **userData)
        return facturaInstance
    
    
    def to_representation(self, obj):
        factura = Factura.objects.get(id=obj.id)
        usuario = User.objects.get(user=obj.id)
        return {
                    'id': factura.id,
                    'username': factura.user,
                    'name': factura.fecha,
                    'usuario': {
                        'id': usuario.id,
                        'balance': usuario.username,
                        'lastChangeDate': usuario.name,
                        'isActive': usuario.email
                    }
                }

