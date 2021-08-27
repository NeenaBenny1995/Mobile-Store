from django.contrib import admin

# Register your models here.
from customer.models import Cart,Orders

admin.site.register(Cart)
admin.site.register(Orders)
