from django.shortcuts import render
from fifth_app.models import UserInfo

def index(request):
    index_dict = {'heading_one':"Welcome!",
        'user_info':"Go to /users to see the list of user information!"}

    return render(request, "fifth_app/index.html",context=index_dict)

def users(request):
    users_list = UserInfo.objects.order_by('firstName')

    users_dict = {'users_heading':"Here are your users:",'user_info':users_list,
        'class_name':UserInfo.class_name}

    return render(request, "fifth_app/users.html", context=users_dict)
