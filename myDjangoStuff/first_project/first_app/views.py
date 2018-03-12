from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>Hello Wolrd!</strong>")

# Create your views here.
