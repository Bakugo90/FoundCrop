#!/usr/bin/python3
"""
"""
from django.shortcuts import render
from crop.models.product import Product


def home(request):
    """
    """
    products = Product.objects.all()
    eats = ['Fruits', 'Beans', 'Grain', 'Legume', 'Tubers', 'Dairy', 'Vegetables', 'Nuts&Kernels', 'Animals']
    return render(request, 'index.html', {'products': products, 'eats': eats})
