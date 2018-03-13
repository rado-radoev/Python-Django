from django.urls import path
from app_three import views

urlpatterns = [
    path("help/", views.help, name='help'),
    path('', views.index, name='index'),

]
