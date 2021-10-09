from rest_framework import serializers
from nogcodevapp.models.usuario import User
from nogcodevapp.models.factura import Factura
#from nogcodevapp.serializers.usuarioSerializer import UsuarioSerializer
from rest_framework.relations import PrimaryKeyRelatedField


class FacturaSerializer(serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Factura
        fields = ['fecha','user']
        
        
    def create(self, validated_data):
        userId = validated_data.pop('user')
        userData = User.objects.get(id=userId)
        facturaInstance = Factura.objects.create(user=userData, **validated_data)
        return facturaInstance
    
    
    def to_representation(self, obj):
        factura = Factura.objects.get(id=obj.id)
        usuario = User.objects.get(id=obj.user)
        return {
                    'id': factura.id,
                    'fecha': factura.fecha,
                    'usuario': {
                        'id': usuario.id,
                        'username': usuario.username,
                    }
                }

