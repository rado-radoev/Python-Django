from django.shortcuts import render

# Create your views here.
def index(request):
    index_dict = {
        'text_import':"This is custom text"
    }
    return render(request, "fourth_app/index.html",context=index_dict)

def help(request):
    help_dict= {
        'insert_error': "Uh, oh, something went horribly wrong!",
        'insert_help': "Was this page helfpul?"
    }

    return render(request, "fourth_app/help.html",context=help_dict)
