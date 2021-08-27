from django import forms
from django.forms import ModelForm
from .models import Brand,Mobile
from customer.models import Orders

class BrandCreationForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "brand_name": forms.TextInput(attrs={"class": "form-control"}),

        }

class BrandUpdateForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "brand_name": forms.TextInput(attrs={"class": "form-control"}),

        }
class SearchForm(forms.Form) :
    brand_name=forms.CharField(max_length=50,widget=(forms.TextInput(attrs={"class":"form-control"})))


class MobileCreationForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
            "mobile_name" :forms.TextInput( attrs={"class": "form-control"}),
            "Brand": forms.Select(attrs={"class": "form-select"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "memory": forms.TextInput(attrs={"class": "form-control"}),
            "os": forms.TextInput(attrs={"class": "form-control"}),
            "specs": forms.TextInput(attrs={"class": "form-control"}),
            # "image": forms.FileInput(attrs={"class": "form-control"}),

        }

class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=["status","user"]