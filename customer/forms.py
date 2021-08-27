from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Orders

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets={
            "first_name": forms.TextInput(attrs={"placeholder": "FirstName"}),
            "email": forms.TextInput(attrs={"placeholder": "email"}),
            "username": forms.TextInput(attrs={"placeholder": "username"}),
            "Password1": forms.TextInput(attrs={"placeholder": "password"}),
            "Password2": forms.TextInput(attrs={"placeholder": "password"}),

        }


class SignInForm(forms.Form):
    username = forms.CharField(max_length=10, widget=(forms.TextInput(attrs={"class": "form-control","placeholder":"username"})))
    password = forms.CharField(max_length=10, widget=(forms.PasswordInput(attrs={"class": "form-control","placeholder":"password"})))

class PlaceOrderForm(forms.Form):
    address=forms.CharField(max_length=120,widget=forms.Textarea(attrs={"class":"form-control"}))

class OrderChangeForm(ModelForm):
    address = forms.CharField(max_length=120, widget=forms.Textarea(attrs={"class": "form-control"}))
    class Meta:
        model=Orders
        fields="__all__"







