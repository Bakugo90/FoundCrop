#!/usr/bin/python3
"""
author      : Victor Doledji
collaborator: Samadou Ouro
file        : prdform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms
from crop.models.product import Product


class PrdForm(forms.ModelForm):
    """
    product formular
    """
    class Meta:
        model = Product
        exclude = ['date']
