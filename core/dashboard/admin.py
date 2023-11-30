from django.contrib import admin
from .models import Stock,PurchaseItem,SalesItem
# Register your models here.

admin.site.register(Stock)
admin.site.register(PurchaseItem)
admin.site.register(SalesItem)
