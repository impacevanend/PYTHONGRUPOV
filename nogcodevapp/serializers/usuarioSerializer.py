from nogcodevapp.models.usuario import User
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','name','email']
        
        
        
       