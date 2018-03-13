from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>Second Project</em>")

def help(request):
    my_dict = {
        'help_django':"Django Help Page!",
    }

    return render(request, "second_app/help.html", context=my_dict)
