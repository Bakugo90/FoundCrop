#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : comment.py
description     : message from models
directory       : foundCrop/crop/models
"""
from django.db import models
from crop.models.user import User


class Comment(models.Model):
    """
    message model
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'message'

