from django.contrib import admin
from icecreamShop.models import Product,Category,CartItem
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CartItem)