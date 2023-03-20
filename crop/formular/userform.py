#!/usr/bin/python3
"""
author      : Victor Doledji
collaborator: Samadou Ouro
file        : commentform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms
from crop.models.user import User


class UserForm(forms.ModelForm):
    """
    user formular
    """
    class Meta:
        model = User
        exclude = ['id', 'created']
