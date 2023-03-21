#!/usr/bin/python3
"""
author      : Victor Doledji
collaborator: Samadou Ouro
file        : productform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms


class LoginForm(forms.Form):
    """
    login
    """
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
