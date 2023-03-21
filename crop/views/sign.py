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
from django.contrib.auth import authenticate, login


def login(request):
    """
    login
    """
    error = False
    if request.method == "POST":
        con = LoginForm(request.POST)
        if con.is_valid():
            username = con.cleaned_data['username']
            password = con.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        con = LoginForm()
        return render(request, 'essaie.html', locals())


def logout(request):
    logout(request)
    return redirect(reverse(login))
