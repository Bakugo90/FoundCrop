#!/usr/bin/python3
"""
author      : Victor Doledji
collaborator: Samadou Ouro
file        : prdform.py
description : formular
directory   : foundCrop/crop/forms
"""
from django import forms
from crop.models.agent import Agent


class AgentForm(forms.Form):
    """
    agent formular
    """
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=70, required=False)
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    address = forms.CharField(max_length=120, required=False)
    status = forms.ChoiceField(choices=(('client', 'Client'), ('trader', 'Trader')))

    def save(self):
        """
        save agent
        """
        agent = Agent()
        agent.first_name = self.cleaned_data['first_name']
        agent.last_name = self.cleaned_data['last_name']
        agent.username = self.cleaned_data['username']
        agent.password = self.cleaned_data['password']
        agent.address = self.cleaned_data['address']
        agent.status = self.cleaned_data['status']
        agent.save()
