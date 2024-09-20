# products/views.py
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# class ProductViewSet(APIView):
#     serializer_class = ProductSerializer

# List all products
@api_view(['GET'])
def get_list(request):
    app = Product.objects.all()
    serializer = ProductSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_product(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
