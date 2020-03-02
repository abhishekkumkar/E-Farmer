from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
# Create your views here.

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")
            price = form.cleaned_data.get("price")
            product = Product(title=title,description=description,price=price)
            product.save()
            return redirect('/')
        else:
            print("No")
            return redirect('/add/product')
    else:
        form = ProductForm(request.POST)
    return render(request, 'add_products.html', {
        'form': form
    })

def product_list(request):
    qs = Product.objects.all()
    context = {
        'qs':qs
    }
    return render(request,'list.html',context)