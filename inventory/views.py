from django.shortcuts import render, redirect
from .models import Product
from django.utils import timezone

def home(request):
    products = Product.objects.all().order_by('-created_at')  #
    return render(request, 'inventory/home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Unnamed Product')  #
        barcode = request.POST.get('barcode', '')
        code_type = request.POST.get('code_type', '')  # Get the code type (QR or Barcode)
        
        if barcode:  # Ensure a barcode was actually scanned
            Product.objects.create(name=name, barcode=barcode, code_type=code_type, created_at=timezone.now())
        
        return redirect('home')
    return redirect('home')
