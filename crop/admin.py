#!/usr/bin/python3
"""
author      : Victor Doledji alias Hydromel
collaborator: Samadou Ouro
file        : admin.py
description : admin file
directory   : foundCrop/crop
"""
from django.contrib import admin
from crop.models.buy import Buy
from crop.models.agent import Agent
from crop.models.product import Product


class AgentAdmin(admin.ModelAdmin):
    """
    agent admin models
    """
    list_display = ('first_name', 'last_name', 'username', 'password', 'address', 'status', 'date_joined')
    list_filter = ('username', 'address', 'date_joined')
    ordering = ('date_joined',)


class PrdAdmin(admin.ModelAdmin):
    """
    product admin models
    """
    list_display = ('agent', 'product_name', 'category', 'price')
    list_filter = ('product_name', 'price', 'category')
    ordering = ('category',)


admin.site.register(Agent, AgentAdmin)
admin.site.register(Product, PrdAdmin)
admin.site.register(Buy)
