from django.db import models
from django.contrib.auth.models import User
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    product_material = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PurchaseItem(models.Model):
    billno = models.AutoField(primary_key=True)
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)
    datetime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate total price based on quantity and perprice
        self.totalprice = self.quantity * self.perprice

        super().save(*args, **kwargs)

    def __str__(self):
        return self.stock.name


class SalesItem(models.Model):
    billno = models.AutoField(primary_key=True)
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)
    datetime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate total price based on quantity and perprice
        self.totalprice = self.quantity * self.perprice

        super().save(*args, **kwargs)

    def __str__(self):
        return self.stock.name


