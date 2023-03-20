#!/usr/bin/python3
"""
author      : Victor Doledji
collaborator: Samadou Ouro
file        : commentform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms
from crop.models.trader import Trader


class TradForm(forms.ModelForm):
    """
    user formular
    """
    class Meta:
        model = Trader
        exclude = ['id', 'created']
