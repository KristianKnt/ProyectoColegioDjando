import imp
from django.urls import path
from . import views


urlpatterns=[
    path('',views.inicio_Pro, name ='inicio_Pro')
]