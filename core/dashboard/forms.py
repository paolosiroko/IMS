from django import forms
from .models import Stock,PurchaseItem


class CreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('name','product_material','product_type','quantity')

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'product_material':forms.TextInput(attrs={'class':'form-control'}),
            'product_type': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('name','product_material','product_type','quantity')

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'product_material':forms.TextInput(attrs={'class':'form-control'}),
            'product_type': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ('stock','quantity','perprice','totalprice')

        widgets ={
            'stock':forms.Select(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'perprice':forms.TextInput(attrs={'class':'form-control'}),
            'totalprice': forms.TextInput(attrs={'class': 'form-control'}),
        }