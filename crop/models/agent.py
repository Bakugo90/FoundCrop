#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : user.py
description     : user from models
directory       : foundCrop/crop/models
"""
from django.db import models


class Agent(models.Model):
    """
    agent user
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=120)
    status = models.CharField(max_length=15, choices=(('client', 'Client'), ('trader', 'Trader')), default='client')
    date_joined = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'agent'
