#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : product.py
description     : product from models
directory       : foundCrop/crop/models
"""
from django.db import models
from crop.models.trader import Trader


class Product(models.Model):
    """
    product model
    """
    CATEGORIES = (('fruits', 'Fruits'), ('beans', 'Beans'), ('grain', 'Grain'),
                  ('legume', 'Legume'), ('tubers', 'Tubers'), ('diary', 'Dairy'),
                  ('vegetables', 'Vegetables'), ('nuts', 'Nuts&Kernels'),
                  ('animals', 'Animals'))
    author = models.ForeignKey(Trader, on_delete=models.CASCADE)
    prd_name = models.CharField(verbose_name='product name', max_length=128, null=False)
    stock = models.IntegerField(default=0)
    description = models.TextField(default='')
    category = models.CharField(max_length=15, choices=CATEGORIES)
    unit_price = models.FloatField(default=0.0)
    picture = models.ImageField(upload_to="img/")
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        managed = False
        db_table = 'product'
