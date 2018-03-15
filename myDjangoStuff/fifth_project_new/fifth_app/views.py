from django.shortcuts import render
from fifth_app.forms import NewUserForm

def index(request):
    index_dict = {'heading_one':"Welcome!",
        'user_info':"Go to /users to sign up!"}

    return render(request, "fifth_app/index.html",context=index_dict)

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid")

    return render(request,"fifth_app/users.html", {'form':form})
