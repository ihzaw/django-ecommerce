from rest_framework import serializers
from .models import User, Product, Order
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = '__all__'
        
class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email_address', 'password', 'full_name', 'phone_number', 'avatar_url')

    def create(self, validated_data):
        user = User.objects.create_user(
            email_address=validated_data['email_address'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name', ''),
            phone_number=validated_data.get('phone_number', ''),
            avatar_url=validated_data.get('avatar_url', ''),
        )
        return user