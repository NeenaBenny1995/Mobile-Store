from django import forms

from owner.models import Mobile
import django_filters

class Mobile_filter(django_filters.FilterSet):
    mobile_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=Mobile
        fields=["mobile_name","price","os"]

