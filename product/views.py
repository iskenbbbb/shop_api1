from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from product.models import Product, Review, Category
from product.serializers import ProductSerializers, ReviewSerializers, CategorySerializers, ProductReviewSerializer, \
    ProductValidateSerializer


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer


class ReviewListAPIView(ListCreateAPIView):  # List -> GET, Create -> POST
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):  # (id) retrieve -> GET, Update -> PUT, Destroy -> DELETE
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductReviewAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReviewSerializer
