# your_app/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
   

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='app/static/product_images/')
    # Add other fields as needed

    def __str__(self):
        return self.name