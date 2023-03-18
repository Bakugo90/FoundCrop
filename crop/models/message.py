#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : message.py
description     : message from models
directory       : foundCrop/crop/models
"""
from django.db import models
from datetime import datetime
from crop.models.user import User


class Message(models.Model):
    """
    message model
    """
    message_id = AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'message'

