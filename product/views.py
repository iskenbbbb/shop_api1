from django.shortcuts import render
from .models import Review
from .models import Category
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .selializers import ProductSerializers
from .selializers import ReviewSerializers
from .selializers import CategorySerializers


@api_view(['GET'])
def ctegory_list_api_view(request):

    category_list = Category.objects.all()
    data = CategorySerializers(instance=category_list, many=True).data

    return Response(data=data)


@api_view(['GET'])
def category_deteil_api_view(request, id):
    try:
        category_deteil = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'massage': 'Category not found'})
    data = CategorySerializers(instance=category_deteil, many=False).data

    return Response(data=data)


@api_view(['GET'])
def product_list_api_view(request):

    product_list = Product.objects.all()
    data = ProductSerializers(instance=product_list, many=True).data

    return Response(data=data)


@api_view(['GET'])
def product_deteil_api_view(request, id):
    try:
        product_deteil = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'massage': 'Product not found'})
    data = ProductSerializers(instance=product_deteil, many=False).data

    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):

    review_list = Review.objects.all()
    data = ReviewSerializers(instance=review_list, many=True).data

    return Response(data=data)


@api_view(['GET'])
def review_deteil_api_view(request, id):
    try:
        review_deteil = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'massage': 'Product not found'})
    data = ReviewSerializers(instance=review_deteil, many=False).data

    return Response(data=data)
