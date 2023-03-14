from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from inventory.models import Product, Order, OrderItem
from inventory.serializers import ProductSerializer, OrderSerializer, UserSerializer
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from datetime import datetime

class OrderListAPIView(APIView):
    """
    List all orders or create a new order
    """
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            orders_data = request.data
            order = Order.objects.create(
                log= orders_data.get('log'),
                customer_name=orders_data.get('customer_name'),
                customer_email=orders_data.get('customer_email'),
                date_updated=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailAPIView(APIView):
    """
    Retrieve, update or delete an order instance
    """
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            order_data = request.data
            order.customer_name = order_data.get('customer_name',order.customer_name)
            order.customer_email = order_data.get('customer_email',order.customer_email)
            order.log = order_data.get('log',order.log)
            order.date_updated = datetime.now()
            order.save()
            return Response({'status':'order updated succefully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OrdersByCustomerAPIView(APIView):
    """
    List all orders for a specific customer
    """
    def get(self, request, customer_email, format=None):
        orders = Order.objects.filter(customer_email=customer_email)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)