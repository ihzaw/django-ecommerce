from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=100)
    password = models.CharField()
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(unique=True)
    avatar_url = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture_url = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.full_name}"