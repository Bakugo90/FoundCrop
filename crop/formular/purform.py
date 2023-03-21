#!/usr/bin/python3
"""
author      : Victor Doledji
collaborator: Samadou Ouro
file        : cmtform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms
from crop.models.purchase import Purchase


class PurForm(forms.ModelForm):
    """
    purchase formular
    """
    class Meta:
        model = Purchase
        fields = ['author', 'products', 'quantity', 'price']
