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
from crop.models.comment import Comment
from crop.models.purchase import Purchase

def prd(request, user_id):
    """
    """
    user = User.objects.get(id=user_id)
    if not user:
        pass
    user_prds = Product.objects.filter(author=user)
    return render(request, 'dash.html', { 'user_prds': user_prds })

def found(request, name):
    """
    """
    founds = Product.objects.filter(prd_name=name)
    return render(request, 'dash.html', { 'founds': founds })

def msgs(request, user_id):
    """
    """
    user = User.objects.get(id=user_id)
    if not user:
        pass
    sms = Comment.objects.filter(id=user_id)
    return render(request, 'dash.html', { 'sms': sms })

def purch(request, user_id):
    """
    """
    user = User.objects.get(id=user_id)
    if not user:
        pass
    purchases = Purchase.objects.filter(id=user_id)
    return render(request, 'dash.html', { 'purchases': purchases })
