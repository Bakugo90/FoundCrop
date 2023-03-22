#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : product.py
description     : product from models
directory       : foundCrop/crop/models
"""
from django.db import models
from crop.models.agent import Agent


class Product(models.Model):
    """
    product model
    """
    CATEGORIES = (('fruits', 'Fruits'), ('beans', 'Beans'), ('grain', 'Grain'),
                  ('legume', 'Legume'), ('tubers', 'Tubers'), ('diary', 'Dairy'),
                  ('vegetables', 'Vegetables'), ('nuts', 'Nuts&Kernels'),
                  ('animals', 'Animals'))
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=128)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    price = models.FloatField(default=0.0)
    picture = models.ImageField(upload_to="crop/static/img/")

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'product'
