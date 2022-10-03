from django.urls import path
from . import views


urlpatterns =[
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('materias',views.materias,name='materias'),
    path('materias/crear',views.crear, name='crear'),
    path('materias/editar',views.editar, name='editar'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('materias/editar/<int:id>',views.editar,name='editar'),
    
]