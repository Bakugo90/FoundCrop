#!/usr/bin/python3
"""
"""
from django.shortcuts import render

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
    sms = Message.objects.filter(id=user_id)
    return render(request, 'dash.html', { 'sms': sms })
