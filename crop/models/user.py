#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : user.py
description     : user from models
directory       : foundCrop/crop/models
"""
from django.db import models


class User(models.Model):
    """
    user model
    """
    first_name = models.CharField(verbose_name='First name', max_length=128, null=True)
    last_name = models.CharField(verbose_name='Last name', max_length=128, default="", null=True)
    username = models.CharField(verbose_name='Username', max_length=128, null=False)
    contact = models.CharField(verbose_name='Contact', max_length=30)
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(verbose_name='Country', max_length=60, default="Togo", null=False)
    city = models.CharField(verbose_name='City', max_length=60, default="Lome", null=False)
    status = models.TextChoices("Client", "Trader")
    about = models.TextField(verbose_name="About", max_length=700, default="", null=True)
    picture = models.ImageField(upload_to="img/")
    password = models.CharField(verbose_name='Password', max_length=128, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'user'

