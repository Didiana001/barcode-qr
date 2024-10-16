from django.shortcuts import render, redirect
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'inventory/home.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        barcode = request.POST['barcode']
        Product.objects.create(name=name, barcode=barcode)
        return redirect('home')
    return redirect('home')
