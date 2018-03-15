from django import forms
from fifth_app.models import UserInfo

class NewUserForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = '__all__'
