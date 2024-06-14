from django.urls import path
from .views import (
    UserListCreate, UserRetrieveUpdateDestroy,
    ProductListCreate, ProductRetrieveUpdateDestroy,
    OrderListCreate, OrderRetrieveUpdateDestroy, 
    RegisterView, LogoutView
)
from . import views

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroy.as_view(), name='order-detail'),
    path('login', views.login_view, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register')
]