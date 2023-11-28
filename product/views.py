from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Review, Category
from product.serializers import ProductSerializers, ReviewSerializers, CategorySerializers, ProductReviewSerializer


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializers = ProductSerializers(product, many=True)
        return Response(serializers.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = ProductSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist():
        return status.HTTP_404_NOT_FOUND
    if request.method == 'GET':
        serializers = ProductSerializers(product)
        return Response(serializers.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializers = ProductSerializers(product, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializers = ReviewSerializers(reviews, many=True)
        return Response(serializers.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ReviewSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializers = ReviewSerializers(reviews)
        return Response(serializers.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializers = ReviewSerializers(reviews, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializers = CategorySerializers(category, many=True)
        return Response(serializers.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
        if request.method == 'GET':
            category = Category.objects.get(id=id)
            serializers = CategorySerializers(category)
            return Response(serializers.data, status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializers = CategorySerializers(category, data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status.HTTP_200_OK)
            return Response(status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            category.delete()
            return Response(status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def product_reviews_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializers = ProductReviewSerializer(product, many=True)
        return Response(serializers.data, status.HTTP_200_OK)
