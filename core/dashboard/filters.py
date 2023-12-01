import django_filters
from django import forms
from django_filters import CharFilter
from .models import *


class StockFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr="icontains", label='Name : ')
    product_type = CharFilter(field_name='product_type', lookup_expr="icontains", label='Product type : ')
    product_material = CharFilter(field_name='product_material', lookup_expr="icontains", label='Product Material : ')

    class Meta:
        model = Stock
        fields = ['name','product_type','product_material']


class PurchaseFilter(django_filters.FilterSet):
    quantity = CharFilter(field_name='quantity', lookup_expr="icontains", label='Quantity : ')

    class Meta:
        model = PurchaseItem
        fields = ['quantity']

class SalesFilter(django_filters.FilterSet):
    quantity = CharFilter(field_name='quantity', lookup_expr="icontains", label='Quantity : ')

    class Meta:
        model = SalesItem
        fields = ['quantity']