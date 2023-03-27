from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from exchange.models import Detail, Product

User = get_user_model()


class UserForm(UserCreationForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'First Name',
            'class': 'form-control'
        }
    ))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Last Name',
            'class': 'form-control'
        }
    ))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Username',
            'class': 'form-control'
        }
    ))
    email = password1 = forms.CharField(label='', widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control'
        }
    ))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }
    ))
    password2 = password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control'
        }
    ))
    
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        }


class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Product Name',
            'class': 'col-md-6'
        }
    ))
    price = forms.DecimalField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'Product Price',
            'class': 'col-md-6'
        }
    ))

    class Meta:
        model = Product
        fields = ('name', 'price', 'picture', 'category')


class DetailForm(forms.ModelForm):
    product_number = forms.CharField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'Count',
            'class':'col-md-6'
        }
    ))
    class Meta:
        model = Detail
        fields = ['product_number']