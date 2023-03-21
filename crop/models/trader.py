#!/usr/bin/python3
"""
author          : Victor Doledji alias Hydromel
collaborator    : Samadou Ouro
file            : trader.py
description     : trader from models
directory       : foundCrop/crop/models
"""
from django.db import models
from datetime import datetime
from crop.models.user import User


class Trader(User):
    """
    trader model
    """
    gps = models.CharField(verbose_name='localisation', max_length=128, null=False)

    class Meta:
        db_table = 'trader'

