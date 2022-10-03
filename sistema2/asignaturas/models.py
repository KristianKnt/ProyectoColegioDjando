from django.db import models

# Create your models here.
class Materia(models.Model):
    id_materias = models.AutoField(primary_key =True)
    materias = models.CharField(max_length=30)
    
    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.materias,self.id_materias)
        