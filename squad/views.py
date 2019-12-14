from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def squad_index(req):
    return HttpResponse('Hello')
