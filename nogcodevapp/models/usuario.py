from django.db import models



    
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    name = models.CharField('Name', max_length = 30)
    email = models.EmailField('Email', max_length = 100)
    
   
    def __str__(self):
        
        return f'Usuario {self.id}: {self.username} {self.name} {self.email}'