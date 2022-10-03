from django.contrib import admin
from .models import Materia
# Register your models here.

#admin.site.register(Materia)

@admin.register(Materia)
class CursoAdmin(admin.ModelAdmin):
    list_display=('id_materias','materias')
    ordering = ('id_materias',)
    search_fields=('materias','id_materias')



