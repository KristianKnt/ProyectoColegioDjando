from django.db import models

from asignaturas.models import Materia
from libreria.models import Estudiante

# Create your models here.
class promedio(models.Model):
    id_estudiante1 =models.ForeignKey(Estudiante,null=True,blank=True, on_delete=models.CASCADE)
    id_materia1 =models.ForeignKey(Materia,null=True,blank=True, on_delete=models.CASCADE)
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    nota3 = models.FloatField()
    promedio = models.FloatField()

    def __str__(self):
        texto = "{0},{1}"
        return texto.format(self.id_estudiante1,self.id_materia1)
