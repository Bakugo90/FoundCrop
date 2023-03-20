#!/usr/bin/python3
"""
author      : Victor Doledji
collaborator: Samadou Ouro
file        : cmtform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms
from crop.models.comment import Comment


class CmtForm(forms.ModelForm):
    """
    formular for comment
    """

    class Meta:
        model = Comment
        fields = ['text']
