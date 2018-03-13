from django.shortcuts import render

# Create your views here.
def index(request):
    text_dict = {
        'text_import':"This is custom text"
    }
    return render(request, "fourth_app/index.html",context=text_dict)
