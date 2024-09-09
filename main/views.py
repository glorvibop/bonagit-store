from django.shortcuts import render
from .models import Product  # Import the Product model

def show_main(request):
    products = Product.objects.all()  # Retrieve all products from the database
    context = {
        'products': products  # Add the products to the context
    }
    return render(request, "main.html", context)
