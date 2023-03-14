from rest_framework import serializers
from .models import Product, Order, OrderItem
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product = Product.objects.get(pk=product_data['id'])
        order_item = OrderItem.objects.create(product=product, **validated_data)
        return order_item


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product_data = item_data.pop('product')
            product = Product.objects.get(pk=product_data['id'])
            OrderItem.objects.create(order=order, product=product, **item_data)
        return order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'address', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            address=validated_data.get('address'),
            phone_number=validated_data.get('phone_number')
        )
        return user