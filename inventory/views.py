# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from .models import Product, Order, OrderItem
# from .serializers import ProductSerializer, OrderSerializer, UserSerializer
# # from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from datetime import datetime

# User = get_user_model()

# class ProductListAPIView(APIView):
#     """
#     List all products or create a new product
#     """
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             product_data = request.data
#             product = Product.objects.create(
#                 name=product_data.get('name'),
#                 price=product_data.get('price'),
#                 description=product_data.get('description'),
#                 quantity=product_data.get('quantity'),
#                 log=product_data.get('log'),
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductDetailAPIView(APIView):
#     """
#     Retrieve, update or delete a product instance
#     """
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             updated_data = request.data
#             product.name = updated_data.get('name', product.name)
#             product.price = updated_data.get('price', product.price)
#             product.description = updated_data.get('description', product.description)
#             product.quantity = updated_data.get('quantity', product.quantity)
#             product.save()
#             return Response({'status': 'Product updated successfully.'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class OrderListAPIView(APIView):
#     """
#     List all orders or create a new order
#     """
#     def get(self, request, format=None):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             # serializer.save()
#             orders_data = request.data
#             order = Order.objects.create(
#                 log= orders_data.get('log'),
#                 customer_name=orders_data.get('customer_name'),
#                 customer_email=orders_data.get('customer_email'),
#                 date_updated=datetime.now())
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class OrderDetailAPIView(APIView):
#     """
#     Retrieve, update or delete an order instance
#     """
#     def get_object(self, pk):
#         try:
#             return Order.objects.get(pk=pk)
#         except Order.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         order = self.get_object(pk)
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         order = self.get_object(pk)
#         serializer = OrderSerializer(order, data=request.data)
#         if serializer.is_valid():
#             order_data = request.data
#             order.customer_name = order_data.get('customer_name',order.customer_name)
#             order.customer_email = order_data.get('customer_email',order.customer_email)
#             order.log = order_data.get('log',order.log)
#             order.date_updated = datetime.now()
#             order.save()
#             return Response({'status':'order updated succefully'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         order = self.get_object(pk)
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class OrdersByCustomerAPIView(APIView):
#     """
#     List all orders for a specific customer
#     """
#     def get(self, request, customer_email, format=None):
#         orders = Order.objects.filter(customer_email=customer_email)
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

# class CustomObtainAuthToken(ObtainAuthToken):
#     """
#     Override ObtainAuthToken to return user object with token
#     """
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'user_id': user.pk})

# class UserListAPIView(APIView):
#     """
#     List all users or create a new user
#     """
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             # token = Token.objects.create(user=user)
#             # token, created = Token.objects.get_or_create(user=user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserDetailAPIView(APIView):
#     """
#     Retrieve, update or delete a user instance
#     """
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
                                                                            
#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class LoginView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

#         if not user.check_password(password):
#             return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST) 
#         # user = request.user
#         token, created = Token.objects.get_or_create(user_id=user.id)

#         return Response({
#             'token': token.key,
#             # 'user_name': user.name,
#             'email': user.email,
#         }, status=status.HTTP_200_OK)