#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : comment.py
description     : comment from models
directory       : foundCrop/crop/models
"""
from django.db import models
from datetime import datetime
from crop.models.user import User


class Comment(models.Model):
    """
    message model
    """
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'comment'

