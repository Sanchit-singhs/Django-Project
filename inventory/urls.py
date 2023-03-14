from django.urls import path
from .api.product_api import ProductListAPIView, ProductDetailAPIView
from .api.order_api import OrderListAPIView, OrderDetailAPIView, OrdersByCustomerAPIView
from .api.user_api import UserListAPIView, UserDetailAPIView, CustomObtainAuthToken, LoginView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api-token-auth'),
    path('register/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('orders/<str:customer_email>/', OrdersByCustomerAPIView.as_view()),
]
