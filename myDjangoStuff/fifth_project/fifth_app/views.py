from django.shortcuts import render

def index(request):
    index_dict = {'heading_one':"Welcome!",
        'user_info':"Go to /users to see the list of user information!"}

    return render(request, "fifth_app/index.html",context=index_dict)

def users(request):
    users_dict = {'users_heading':"Here are your users:"}

    return render(request, "fifth_app/users.html", context=users_dict)
