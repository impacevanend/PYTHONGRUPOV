from django.db import models



    
class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    
    
    def __str__(self):
        
        return f'Categoria {self.id}: {self.descripcion}'
    
   