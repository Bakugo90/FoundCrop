#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : product.py
description     : product from models
directory       : foundCrop/crop/models
"""
from django.db import models
from datetime import datetime
from crop.models.trader import Trader
from crop.models.comment import Comment


class Product(models.Model):
    """
    product model
    """
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Trader, on_delete=models.CASCADE)
    prd_name = models.CharField(verbose_name='product name', max_length=128, null=False)
    stock = models.IntegerField(default=0)
    description = models.TextField(default='')
    categorie = models.CharField(max_length=30, null=False)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    unit_price = models.FloatField(verbose_name='unit price', default=0.0)
    picture = models.ImageField()

    class Meta:
        managed = False
        db_table = 'product'

