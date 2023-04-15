from django import forms
from .models import Login
class LoginFrom(forms.Form):
    username = forms.CharField(max_length=250,label="name")
    password = forms.CharField(max_length=250,label="password",
                               widget=forms.PasswordInput)
class LoginForm1(forms.ModelForm):
    class Meta:
        model=Login
        #fields="__all__"
        fields=["username"]