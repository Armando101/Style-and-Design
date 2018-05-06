from django.db import models
from django.utils import timezone

# Create your models here. Va

class Post(models.Model):
    """
    Modelo para almacenar los posts
    """
    autor = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    titulo = models.CharField(max_length= 200)
    texto = models.TextField()
    fechaCreacion = models.DateTimeField(
        default = timezone.now
    )
    fechaPublicacion = models.DateTimeField(
        blank= True, null = True
    )

    def publicar(self):
        """
        Método para obtener la fecha de publicación
        cuando se publique algún Post
        """
        self.fechaPublicacion = timezone.now()
        self.save()

    #Método mágico que nos permite castear un objeto a una cadena
    def __str__(self):
        return self.titulo



class Usuario(models.Model):
    username = models.CharField(max_length=20, null=False, primary_key=True)
    password = models.CharField(max_length=100, null=False)
    nombre = models.CharField(max_length=30, null=False)
    apellidoP = models.CharField(max_length=30, null=False)
    apellidoM = models.CharField(max_length=30, null=False)
    numero = models.PositiveIntegerField( null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.username




