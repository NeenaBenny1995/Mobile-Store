from django.db import models
from owner.models import Mobile

# Create your models here.

class Cart(models.Model):
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    user=models.CharField(max_length=50)
    options=(("in_cart","in_cart"),("order_placed","order_placed"),("canceled","canceled"))
    status=models.CharField(max_length=50,choices=options,default="in_cart")

class Orders(models.Model):
    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    address=models.CharField(max_length=250)
    options=(
        ("order_placed","order_placed"),
        ("cancelled","cancelled"),
        ("dispated","dispated"),
        ("in_transit","in_transit"),
        ("ready_to_deliver","ready_to_deliver"),
        ("delivered","delivered"),)
    status=models.CharField(max_length=120,choices=options,default="order_placed")
    user=models.CharField(max_length=120)

