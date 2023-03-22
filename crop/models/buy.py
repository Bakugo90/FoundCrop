"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : purchase.py
description     : purchase from models
directory       : foundCrop/crop/models
"""
from django.db import models
from crop.models.product import Product
from crop.models.agent import Agent


class Buy(models.Model):
    """
    buy
    """
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0.0)
    publish = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'buy'
