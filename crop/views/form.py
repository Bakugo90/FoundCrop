#!/usr/bin/python3
"""
author      : Victor Doledji alias Hydromel
collaborator: Samadou Ouro
file        : form.py
description : formular
directory   : foundCrop/crop/views
"""
from django.shortcuts import render, redirect
from crop.formular.cmtform import CmtForm
from crop.formular.prdform import PrdForm
from crop.formular.purchform import PurchForm
from crop.formular.userform import UserForm
from crop.formular.tradform import TradForm


def signinUser(request):
    """
    signin
    """
    if request.method == "POST":
        sign = UserForm(request.POST, request.FILES)
        if sign.is_valid():
            sign.save()
            return redirect('/login')
        else:
            return render(request, 'index.html', {'sign': sign})
    else:
        sign = UserForm()
        return render(request, 'index.html', {'sign': sign})


def signinTrader(request):
    """
    signin
    """
    if request.method == "POST":
        sign = TradForm(request.POST, request.FILES)
        if sign.is_valid():
            sign.save()
            return redirect('/login')
        else:
            return render(request, 'index.html', {'sign': sign})
    else:
        sign = TradForm()
        return render(request, 'index.html', {'sign': sign})


def msg(request):
    """
    message comment
    """
    if request.method == "POST":
        cmt = CmtForm(request.POST)
        if cmt.is_valid():
            cmt.save()
            return render(request, 'index.html')
        else:
            return render(request, 'index.html', {'cmt': cmt})
    else:
        cmt = CmtForm()
        return render(request, 'index.html', {'cmt': cmt})


def add_product(request):
    """
    add product
    """
    if request.method == "POST":
        add = PrdForm(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('/home')
        else:
            return render(request, 'dashboard.html', {'add': add})
    else:
        add = PrdForm()
        return render(request, 'dashboard.html', {'add': add})


def buy(request):
    """
    buy
    """
    if request.method == "POST":
        pay = PurchForm(request.POST)
        if pay.is_valid():
            pay.save()
            sms = "payment success!!!"
            return render(request, 'index.html', {'sms': sms})
        else:
            return render(request, 'index.html', {'pay': pay})
    else:
        pay = PurchForm()
        return render(request, 'index.html', {'pay': pay})
