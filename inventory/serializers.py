from rest_framework import serializers
from .models import Product, Order, OrderItem
from django.contrib.auth import get_user_model
from django.db.models import Prefetch

User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['deleted_at', 'created_by', 'updated_by', 'created_at', 'updated_at']


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        exclude = ['deleted_at', 'created_by', 'updated_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product = Product.objects.get(pk=product_data['id'])
        order_item = OrderItem.objects.create(product=product, **validated_data)
        return order_item

class OrderSerializer(serializers.ModelSerializer):
    num_products = serializers.SerializerMethodField()
    product_names = serializers.SerializerMethodField()
    items = OrderItemSerializer(many=True)
    # staff_status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        # exclude = ['deleted_at', 'created_by', 'updated_by', 'created_at', 'updated_at']
        fields = '__all__'

    def get_num_products(self, obj):
        items = obj.items.all()
        # print(self.context.get('request').user.is_staff)
        num_products = items.count()
        return num_products

    def get_product_names(self, obj):
        # items = obj.items.all()
        items = obj.items.select_related('product')
        product_names = [item.product.name for item in items]
        return product_names
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        staff_status = self.context.get('request').user.is_staff
        
        if not staff_status:
            pop_items = ['deleted_at', 'created_by', 'updated_by', 'created_at', 'updated_at', 'items', 'id']
            for pops in pop_items:
                representation.pop(pops)
        return representation
    

class OrderSerializerPost(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        exclude = ['deleted_at', 'created_by', 'updated_by', 'created_at', 'updated_at']
        prefetch_related = Prefetch('product', queryset=Product.objects.only('id', 'name'))
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product_data = item_data.pop('product')
            order_data = item_data.pop('order')
            product = Product.objects.get(name=product_data['name'])
            item = OrderItem.objects.create(product=product, order=order, **item_data)

        order.total_bill = sum(item.total_price for item in order.items.all())
        order.save()

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