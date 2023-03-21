#!/usr/bin/python3
"""
author      : Victor Doledji alias Hydromel
collaborator: Samadou Ouro
file        : dash.py
description : views file
directory   : foundCrop/crop/views
"""
from django.shortcuts import render
from crop.models.user import User
from crop.models.product import Product
from crop.models.purchase import Purchase
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    """
    dashboard view
    """
    purchases = Purchase.objects.filter(products=request.user)
    nb_sal = 0
    price_rev = 0.0
    for prd in purchases:
        if prd.date.date() == datetime.date():
            nb_sal += prd.quantity
        if prd.date.year == datetime.year and prd.date.month == datetime.month:
            price_rev += prd.price

    products = Product.objects.filter(author=request.user)
    total_price = 0.0
    for prd in products:
        total_price += prd.unit_price * prd.stock
        sales = (nb_sal, nb_sal / len(products))

    revenue = (price_rev, price_rev / total_price)

    dash = {'sales': sales, 'revenue': revenue}
    return render(request, 'dashboard.html', context=dash)


@login_required
def profile(request):
    """
    profile view
    """
    products = Product.objects.filter(author=request.user)
    context = {'products': products}
    return render(request, 'profile.html', context)
