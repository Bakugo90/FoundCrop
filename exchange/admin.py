"""
admin models
"""
from django.contrib import admin
from .models import Card, Client, Command, Detail, Product, Provider, User

# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Card)
admin.site.register(Command)
admin.site.register(Detail)
