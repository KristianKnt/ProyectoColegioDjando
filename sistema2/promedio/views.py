from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render

# Create your views here.
def inicio_Pro(request):
    return HTTPResponse("Hola usuario")