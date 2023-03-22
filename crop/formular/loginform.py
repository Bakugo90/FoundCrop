#!/usr/bin/python3
"""
author      : Victor Doledji alias Hydromel
collaborator: Samadou Ouro
file        : loginform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms


class LoginForm(forms.Form):
    """
    login
    """
    username = forms.CharField(label="username", max_length=30)
    password = forms.CharField(label="password", widget=forms.PasswordInput)
