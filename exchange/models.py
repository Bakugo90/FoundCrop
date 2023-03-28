from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from exchange import CATEGORIES, COUNTRY, SEXE

# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=132, default='')
    picture = models.EmailField(upload_to='images', blank=True)
    country = models.CharField(max_length=132, default='------------', choices=COUNTRY)
    state = models.CharField(max_length=16, default='')
    sexe = models.CharField(max_length=1, choices=SEXE, default='')
    is_prof = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.username


class Client(User):
    is_client = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "{}:{}".format('client', self.username)


class Professional(User):
    is_prof = is_client = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "{}:{}".format('provider', self.username)


class Product(models.Model):
    professional = models.ForeignKey(Professional, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='images', blank=True)
    category = models.CharField(choices=CATEGORIES, max_length=50)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('productUpdate', kwargs={'prd_id': self.pk})


class Card(models.Model):
    user = models.ForeignKey(User, related_name='cards', on_delete=models.PROTECT)
    zip_code = models.CharField(max_length=16)
    card_name = models.CharField(max_length=16)
    card_number = models.CharField(max_length=32)
    expiration = models.DateField()
    cvv = models.CharField(verbose_name='CVV', max_length=32)

    def __str__(self) -> str:
        return "MasterCard:{}".format(self.user)


class Command(models.Model):
    card = models.ForeignKey(Card, related_name='commands', on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=50, decimal_places=2)
    # pour savoir sur quel commande ajouter le produits
    valid = models.BooleanField(default=True)
    # pour savoir si la command est payer
    pay = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{}-{}".format('Command', self.card.user.username)

    @property
    def total(self):
        total = 0
        details = Detail.objects.filter(active=True)
        for detail in details:
            total += detail.total()
        return round(total, 2)


class Detail(models.Model):
    product = models.ForeignKey(Product, related_name='details', on_delete=models.PROTECT)
    cmd = models.ForeignKey(Command, related_name='details', on_delete=models.PROTECT)
    count = models.IntegerField()
    # pour ne pas ajouter des produits d'ancien facture
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "{}:{}:{}".format(self.cmd, self.product, self.count)

    @property
    def total(self):
        return round(self.product.price * self.count, 2)
    
    def get_absolute_url(self):
        return reverse('Update_to_cart', kwargs={'detail_id': self.pk})
