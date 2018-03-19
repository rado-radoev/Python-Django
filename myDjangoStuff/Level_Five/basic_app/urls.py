from django.urls import path, inlcude, re_path
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
    re_path(r'^register/$',view.register, name='register')
]
