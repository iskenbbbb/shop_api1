from rest_framework import serializers
from .models import Product, Category, Review



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = 'title rating'.split()
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()
        # fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = 'title rating'.split()
        fields = '__all__'

