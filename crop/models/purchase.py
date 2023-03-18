#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : purchase.py
description     : purchase from models
directory       : foundCrop/crop/models
"""
from django.db import models
from datetime import datetime
from crop.models.user import User
from crop.models.product import Product


class Purchase(models.Model):
    """
    purchase model
    """
    purchase_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Quantity', default=0)
    price = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'purchase'

