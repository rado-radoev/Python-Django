from django.urls import include, re_path
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
    re_path(r'^register/$',views.register, name='register'),
]
