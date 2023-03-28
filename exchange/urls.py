from django.contrib import admin
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
    path('product/del/<int:prd_id>',  productDel, name='productDel'),
    path('product/update/<int:prd_id>',  productUpdate, name='productUpdate'),

    path('cmd/view',  cmdView, name='cmdview'),
    path('add_to_cart/<int:detail_id>',  Add_to_cart, name='add_to_cart'),
    path('cmd/del/<int:cmd_id>',  cmdDel, name='cmdDel'),
    path('del_to_cart/<int:detail_id>',  del_to_cart, name='del_to_cart'),
    path('update_to_cart/<int:details_id>',  Update_to_cart, name='update_to_cart'),
    path('buy',  buy, name='buy'),

    path('signin',  signin, name='signin'),
    path('signup',  signup, name='signup'),
]
