from django.urls import path
from fifth_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'users/', views.users, name='users'),
]
