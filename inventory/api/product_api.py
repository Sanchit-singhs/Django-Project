from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from inventory.models import Product
from inventory.serializers import ProductSerializer

class ProductListAPIView(APIView):
    """
    List all products or create a new product
    """
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product_data = request.data
            product = Product.objects.create(
                name=product_data.get('name'),
                price=product_data.get('price'),
                description=product_data.get('description'),
                quantity=product_data.get('quantity'),
                log=product_data.get('log'),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    """
    Retrieve, update or delete a product instance
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            updated_data = request.data
            product.name = updated_data.get('name', product.name)
            product.price = updated_data.get('price', product.price)
            product.description = updated_data.get('description', product.description)
            product.quantity = updated_data.get('quantity', product.quantity)
            product.save()
            return Response({'status': 'Product updated successfully.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
