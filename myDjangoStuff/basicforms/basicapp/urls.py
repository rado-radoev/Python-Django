from django.urls import path
from basicapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/',views.form, name='form'),

]
