#!/usr/bin/python3
"""
"""
from django.shortcuts import render
from crop.models.product import Product


def home(request):
    """
    home page for no_user
    """
    products = []
    if request.method == "GET" and len(request.GET['searching']) > 0:
        searching = request.GET['searching']
        searching = str(searching).split()
        for string in searching:
            for product in Product.objects.filter(prd_name=string):
                products.append(product)
    else:
        products = Product.objects.all()
    eats = ['Fruits', 'Beans', 'Grain', 'Legume', 'Tubers', 'Dairy', 'Vegetables', 'Nuts&Kernels', 'Animals']
    return render(request, 'index.html', {'products': products, 'eats': eats})

