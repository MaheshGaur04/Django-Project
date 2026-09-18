from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product


@api_view(['GET', 'POST'])
def product(req):
    if req.method == 'GET':
        rows = Product.objects.values('id', 'name', 'price')
        return Response(list(rows))

    name = req.data.get('name')
    price = req.data.get('price')

    if not name or price is None:
        return Response(
            {'error': 'Please enter a name and price.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    item = Product.objects.create(name=name, price=price)
    return Response(
        {'id': item.id, 'name': item.name, 'price': item.price},
        status=status.HTTP_201_CREATED,
    )
