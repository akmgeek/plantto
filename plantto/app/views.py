
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile , Product, Category
from .cart import Cart

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            address = request.POST.get('address')  # Get the address from the form
            user_profile = UserProfile.objects.create(user=user, address=address)
            user_profile.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your home view name
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
        else:
             messages.error(request,'Username or Password not correct')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})



@login_required
def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout

def home(request):
    # username = request.user.username
    # return render(request, 'app/home.html', {'username': username})  # Create home.html in your templates folder
    username = request.user.username
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'username': username, 'products': products, 'categories': categories}
    return render(request, 'app/home.html', context)

def category_products(request, category_id):
   # Get the category or return a 404 response if it doesn't exist
    category = get_object_or_404(Category, id=category_id)

    # Get all products belonging to the specified category
    products = Product.objects.filter(category=category)

    # You can add additional logic or data processing here if needed

    # Pass the category and products to the template
    context = {'category': category, 'products': products}
    return render(request, 'app/product_list.html', context)


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'app/product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'app/product_detail.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Assume you have a cart object, modify this part based on your cart implementation
    cart = Cart(request)
    cart.add(product=product)

    # return redirect('cart_view')
    # Return the cart quantity in JSON format
    return JsonResponse({'cart_quantity': cart.get_total_quantity()})

def cart_view(request):
    cart = Cart(request)
    return render(request, 'app/cart.html', {'cart': cart})

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart_view')

def contact(request):
    return render(request, 'app/contact.html')