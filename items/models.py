from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password, check_password as django_check_password

class UserManager(BaseUserManager):
    def create_user(self, email_address, password=None, **extra_fields):
        if not email_address:
            raise ValueError('The Email field must be set')
        email_address = self.normalize_email(email_address)
        user = self.model(email_address=email_address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_address, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email_address, password, **extra_fields)
class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(unique=True)
    avatar_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    def __str__(self):
        return self.full_name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        return django_check_password(raw_password, self.password)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    full_description = models.CharField()
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