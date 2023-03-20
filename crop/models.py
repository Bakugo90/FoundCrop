#!/usr/bin/python3
"""
author      : Victor Doledji alias Hydromel
collaborator: Samadou Ouro
file        : admin.py
description : admin file
directory   : foundCrop/crop
"""
from django.contrib import admin
from crop.models.user import User
from crop.models.trader import Trader
from crop.models.comment import Comment
from crop.models.purchase import Purchase
from crop.models.product import Product


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'contact', 'email', 'country', 'city', 'status', 'password')
    list_filter = ('username', 'email', 'created')
    ordering = ('first_name', 'created')
    search_fields = ('username', 'email', 'country', 'city', 'status')


class TraderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'contact', 'email', 'country', 'city', 'status',
                    'password', 'gps')
    list_filter = ('username', 'email', 'created', 'gps')
    ordering = ('first_name', 'created')
    search_fields = ('username', 'email', 'country', 'city', 'status', 'gps')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'publish')
    list_filter = ('author', 'publish')
    ordering = 'publish'
    search_fields = ('text', 'author', 'publish')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('author', 'products', 'quantity', 'price', 'date')
    list_filter = ('author', 'date')
    ordering = 'date'
    search_fields = 'products'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('author', 'prd_name', 'stock', 'description', 'category', 'comments', 'unit_price')
    list_filter = ('author', 'prd_name', 'category', 'unit_price')
    ordering = ('category', 'prd_name', 'unit_price')
    search_fields = ('prd_name', 'category', 'unit_price')


admin.site.register(User, UserAdmin)
admin.site.register(Trader, TraderAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Product, ProductAdmin)
