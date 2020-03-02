from django import forms

class ProductForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Product Name",}),label ='Product Name')
    description = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Product Description",}),label ='Product Description',required=False)
    price = forms.DecimalField(widget = forms.NumberInput (attrs={"class": "form-control", "placeholder":"Product price",}), label ='Product Price',max_digits=8,decimal_places=2, min_value=0)

    