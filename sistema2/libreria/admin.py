from django.contrib import admin
from .models import Estudiante
# Register your models here.

@admin.register(Estudiante)
class CursoAdmin(admin.ModelAdmin):
    list_display=('id_estudiante','nombre')
    ordering = ('id_estudiante',)
    search_fields=('nombre','id_estudiante')


#admin.site.register(Estudiante)
