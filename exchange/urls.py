from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from exchange.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),

    path('dashboard', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    path('logout',  output, name='logout'),

    path('product/view',  productView, name='productView'),
    path('product/add',  productAdd, name='productAdd'),
    path('product/del',  productDel, name='productDel'),
    path('product/update',  productUpdate, name='productUpdate'),

    path('cmd/view',  cmdView, name='cmdview'),
    path('add_to_cart/<int:product_id>',  Add_to_cart, name='add_to_cart'),
    path('cmd/del',  cmdDel, name='cmdDel'),
    path('del_to_cart',  del_to_cart, name='del_to_cart'),
    path('update_to_cart',  Update_to_cart, name='update_to_cart'),
    path('buy',  buy, name='buy'),

    path('signin',  signin, name='signin'),
    path('signup',  signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)