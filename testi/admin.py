from django.contrib import admin

from  .models import Product, Firm
# Register your models here.

admin.site.register(Firm)
admin.site.register(Product)
