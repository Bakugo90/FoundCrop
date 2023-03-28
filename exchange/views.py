from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from exchange import CATEGORIES, COUNTRY
from .models import Card, Command, Detail, Product
from .forms import DetailForm, UserForm

# Create your views here.


# home page
def home(request):
    """
    method of index.htm file
    """
    products = Product.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search')
        if search is not None:
            products = Product.objects.filter(name__icontains=search)
        
    context = {
        'search': search,
        'food': CATEGORIES,
        'products': products
    }
    return render(request, 'index.html', context)


# -----------------------------------------------------------------------------

# user fonction


# dashbord
def dashboard(request):
    """
    dashboard statistiques
    """
    if request.user.is_client:
        card  = Card.objects.get(user=request.user)
        item = Command.objects.filter(user=card.user)
        # nbre de command effectuer
        sale = item.count()
        # frais total de tous les command
        revenue = sum([obj.total() for obj in item])
        customers = 1
    else:
        products = Product.objects.filter(provider=request.user)
        details = Detail.objects.all()
        # nombre total de vente
        sale = 0
        # gains total
        revenue = 0
        # nbre total de client
        customers = 0
        for detail in details:
            if detail.product.Provider in [prod.provider for prod in products]:
                revenue += detail.product.price
                sale += 1
        customers = len(set([cmd.card.user for cmd in Command.objects.all()]))

    context = {
        'sale' : sale,
        'revenue' : revenue,
        'customers': customers
    }
    return render(request, 'auth/dashboard.html', context)


# profile
def profile(request):
    """
    update profile
    """

    form = UserForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.first_name = request.POST['']
        form.last_name
        form.username
        form.email
        form.address
        form.
        form.
        form.
        form.
        form.
        form.
        form.
        form.
        form.
        form.
        form.

    context = {
        'form': form,
        'country': COUNTRY,
        'sexe': sexe
    }
    return render(request, 'auth/profile.html', context)


# logout
def output(request):
    """
    deconnexion
    """
    logout(request)
    return redirect('home')
# --------------------------------------------------------------------------------

# product


# view
def productView(request):

    context = {

    }
    return render(request, 'product/view.html', context)


#add
def productAdd(request):

    context = {

    }
    return render(request, 'product/add.html', context)


# del
def productDel(request):

    context = {

    }
    return render(request, 'product/del.html', context)


# update
def productUpdate(request):

    context = {

    }
    return render(request, 'product/update.html', context)

# ---------------------------------------------------------------------------------

# command

# view
def cmdView(request):

    context = {

    }
    return render(request, 'cmd/view.html', context)


#add
def Add_to_cart(request, product_id):
    """
    add a product to cart
    """
    product = get_object_or_404(Product, id=product_id)

    form = DetailForm()
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.cmd = Command.objects.get(valid=True)
            obj.product = product
            obj.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'cmd/add_to_cart.html', context)


# del
def cmdDel(request):

    context = {

    }
    return render(request, 'cmd/del.html', context)


def del_to_cart(request):

    context = {

    }
    return render(request, 'cmd/del_to_cart.html', context)


# update
def Update_to_cart(request):

    context = {

    }
    return render(request, 'cmd/update_to_cart.html', context)


# buy
def buy(request):

    context = {

    }
    return render(request, 'cmd/buy.html', context)

# --------------------------------------------------------------------------

# login
def signin(request):
    """
    all user login from
    """
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'username or password invalid'
    
    context = {
        'error': error
    }
    return render(request, 'signin.html', context)


# register
def signup(request):
    """
    all user register form
    """
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)
