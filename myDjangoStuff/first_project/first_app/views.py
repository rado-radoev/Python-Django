from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me':"Hello I am from views.py !!!",
        'paragraph_text':"This is a paragraph_text"}

    return render(request, 'first_app/index.html', context=my_dict)
