#!/usr/bin/python3
"""
author      : Victor Doledji
collaborator: Samadou Ouro
file        : commentform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms
from crop.models.purchase import Purchase


class PurchForm(forms.ModelForm):
    """
    purchase formular
    """
    class Meta:
        model = Purchase
        fields = ['products', 'quantity', 'price']
