"""
models forms
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from exchange import CATEGORIES, COUNTRY, SEXE
from exchange.models import Detail, Product, Card

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

    email = forms.CharField(label='', widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control'
        }
    ), required=False)

    address = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Address',
            'class': 'form-control',
            
        }
    ), required=False)

    picture = forms.ImageField(label='', widget=forms.ClearableFileInput(
        attrs={
            'placeholder': 'entry your image',
            'class': 'form-control'
        }
    ), required=False)

    country = forms.Select(attrs={
        'placeholder': 'Country',
        'class': 'form-control'
    }, choices=COUNTRY)

    state = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'State',
            'class': 'form-control',
        }
    ), required=False)

    sexe = forms.CharField(label='', widget=forms.CheckboxInput(
        attrs={
            'placeholder': 'Sexe',
            'class': 'form-control'
        },
        check_test=SEXE
    ), required=False)

    is_prof = forms.BooleanField(label='Swicth to professional acount', widget=forms.CheckboxInput(
        check_test=(('Y', 'Yes'), ('N', 'No'))
    ), disabled=True, required=False)

    is_client = forms.BooleanField(label='Swicth to client acount', widget=forms.CheckboxInput(
        check_test=(('Y', 'Yes'), ('N', 'No'))
    ), disabled=False, required=False)

    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(label='', widget=forms.PasswordInput(
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
            'address',
            'picture',
            'country',
            'state',
            'sexe',
            'is_prof',
            'is_client',
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

    picture = forms.ImageField(label='', widget=forms.ClearableFileInput(
        attrs={
            'placeholder': 'Product Image',
            'class': 'form-control'
        }
    ))

    category = forms.Select(attrs={
        'placeholder': 'Category',
        'class': 'form-control'
    }, choices=CATEGORIES)
    
    class Meta:
        model = Product
        fields = ('name', 'price', 'picture', 'category')


class CardForm(forms.ModelForm):
    zip_code = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Zip Code',
            'class': 'form-control'
        }
    ))

    card_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Card Name',
            'class': 'form-control'
        }
    ))

    card_number = forms.CharField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'Card Number',
            'class': 'form-control'
        }
    ))

    expiration = forms.CharField(label='', widget=forms.DateInput(
        attrs={
            'placeholder': 'Expiration',
            'class': 'form-control'
        }
    ))

    cvv = forms.CharField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'CVV',
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Card
        fields = ['zip_code', 'card_name', 'card_number', 'expiration', 'cvv']


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
