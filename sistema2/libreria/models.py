from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key =True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.nombre,self.id_estudiante)







    