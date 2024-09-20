# products/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView


class ProductViewSet(APIView):
    serializer_class = ProductSerializer

    # List all products
    def get_list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    # Create a new product
    def create_product(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve a specific product
    def retrieve_by_id(self, request, pk=None):
        queryset = Product.objects.filter(pk=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    # Update a specific product
    def update_by_id(self, request, pk=None):
        product = Product.objects.filter(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific product
    def destroy_by_id(self, request, pk=None):
        product = Product.objects.filter(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
