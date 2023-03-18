#!/usr/bin/python3
"""
"""
from django.shortcuts import render
from crop.models.product import Product

def home(request):
    """
    """
    products = Products.objects.all()
    return render(request, 'index.html', { 'products': products })
