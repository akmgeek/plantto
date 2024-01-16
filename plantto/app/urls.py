# your_app/urls.py

from django.urls import path
from .views import (register,
                    home,
                    user_login, user_logout,
                    product_list, category_products, product_detail,
                    add_to_cart, cart_view , remove_from_cart, contact, about)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'), 
    path('contact/', contact, name='contact'), 
    path('about/', about, name='about'), 
     
    path('category/<int:category_id>/', category_products, name='category_products'), 
    path('products/', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    
    # View and edit cart
    path('cart/', cart_view, name='cart_view'),
    
        # Remove items from the cart
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    # Add more URLs as needed
]
