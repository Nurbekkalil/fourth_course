from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def products_item_view(request, id):
    product = Product.objects.get(id=id)
    data = ProductSerializer(product).data

    return Response(data=data)