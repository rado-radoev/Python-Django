from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    index_dict = {
        "index_insert": "Welcome to django!"
    }

    return render(request, "app_three/index.html",context=index_dict)

def help(request):
    help_dict = {
        "help_insert":"This is a help page!"
    }

    return render(request, "app_three/help.html",context=help_dict)
