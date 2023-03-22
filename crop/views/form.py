#!/usr/bin/python3
"""
author      : Victor Doledji alias Hydromel
collaborator: Samadou Ouro
file        : form.py
description : formular
directory   : foundCrop/crop/views
"""
from django.shortcuts import render, redirect
from crop.formular.prdform import PrdForm
from crop.formular.buyform import BuyForm
from crop.formular.agentform import AgentForm
from django.contrib.auth.decorators import login_required


def signin(request):
    """
    signin
    """
    if request.method == "POST":
        sign = AgentForm(request.POST, request.FILES)
        if sign.is_valid():
            sign.save()
            return redirect('/connect')
        else:
            return render(request, 'sign.html', {'sign': sign})
    else:
        sign = AgentForm()
        return render(request, 'sign.html', {'sign': sign})


@login_required
def add_product(request):
    """
    add product
    """
    if request.method == "POST":
        add = PrdForm(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('/product')
        else:
            return render(request, 'addingProduct.html', {'add': add})
    else:
        add = PrdForm()
        return render(request, 'addingProduct.html', {'add': add})


@login_required
def buy(request):
    """
    buy
    """
    if request.method == "POST":
        pay = BuyForm(request.POST)
        if pay.is_valid():
            pay.save()
            sms = "payment success!!!"
            return render(request, 'index.html', {'sms': sms})
        else:
            return render(request, 'index.html', {'pay': pay})
    else:
        pay = BuyForm()
        return render(request, 'index.html', {'pay': pay})
