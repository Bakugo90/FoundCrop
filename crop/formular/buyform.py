#!/usr/bin/python3
"""
author      : Victor Doledji
collaborator: Samadou Ouro
file        : cmtform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms
from crop.models.buy import Buy


class BuyForm(forms.ModelForm):
    """
    purchase formular
    """

    class Meta:
        model = Buy
        exclude = []
