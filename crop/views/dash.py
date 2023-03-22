#!/usr/bin/python3
"""
author      : Victor Doledji alias Hydromel
collaborator: Samadou Ouro
file        : dash.py
description : views file
directory   : foundCrop/crop/views
"""
from django.shortcuts import render
from crop.models.product import Product
from crop.models.agent import Agent
from crop.models.buy import Buy
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    """
    dashboard view
    """
    buys = Buy.objects.filter(agent=request.user)
    nb_sal = 0
    price_rev = 0.0
    nb_cust = 0
    sales = 0
    for prd in buys:
        if prd.date.date() == datetime.date():
            nb_sal += prd.quantity
        if prd.date.year == datetime.year and prd.date.month == datetime.month:
            price_rev += prd.price

    products = Product.objects.filter(agent=request.user)
    total_price = 0.0
    for prd in products:
        total_price += prd.unit_price * prd.stock
        sales = (nb_sal, nb_sal / len(products))

    for product in products:
        nb_cust += len(set([purchase.author for purchase in Buy.objects.filter(products=product)]))

    revenue = (price_rev, price_rev / total_price)
    cust = (nb_cust, Agent.objects.all())
    dash = {'sales': sales, 'revenue': revenue, 'cust': cust}
    return render(request, 'dashboard.html', context=dash)


@login_required
def profile(request):
    """
    profile view
    """
    return render(request, 'profile.html')
