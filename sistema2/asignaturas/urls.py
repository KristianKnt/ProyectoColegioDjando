import imp
from django.urls import path
from . import views


urlpatterns=[
    path('',views.inicio_Asig, name ='inicio_Asig')
]