#!/usr/bin/python3
"""
author      : Victor Doledji alias Hydromel
collaborator: Samadou Ouro
file        : form.py
description : formular
directory   : foundCrop/crop/views
"""
from django.shortcuts import render, redirect
from crop.formular.loginform import LoginForm
from django.contrib.auth import authenticate, login, logout


def connect(request):
    """
    login
    """
    if request.method == "POST":
        con = LoginForm(request.POST)
        if con.is_valid():
            username = con.cleaned_data['username']
            password = con.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard")
        else:
            return render(request, 'login.html', locals())
    else:
        con = LoginForm()
        return render(request, 'login.html', locals())


def outlog(request):
    """
    logout
    """
    logout(request)
    return redirect('/connect')
