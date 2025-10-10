from django.contrib import admin
from .models import User, Category, Product, Customer, Sale, SaleItem

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SaleItem)