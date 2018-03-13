from django.conf import path
from fourth_app import views

urlpatterns = [
    path('', views.index, name='index')
]
