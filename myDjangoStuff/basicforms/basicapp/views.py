from django.shortcuts import render
from . import forms

def index(request):
    index_list = {
        'welcome_message':"Welcome to Home Page!",
        'welcome_subtitle':"This will be a django forms test",
    }
    return render(request, "basicapp/index.html",context=index_list)


def form(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success!")
            print("Name: {}".format(form.cleaned_data['name']))
            print("Email: {}".format(form.cleaned_data['email']))
            print("Text: {}".format(form.cleaned_data['text']))

    return render(request, 'basicapp/form_page.html', {'form':form})
