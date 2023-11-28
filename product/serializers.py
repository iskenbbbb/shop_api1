from rest_framework import serializers

from product.models import Category, Product, Review


class CategorySerializers(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category

        fields = ('id', 'name', 'product_count')

    def get_product_count(self, obj):
        return obj.products.count()


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category')


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review

        fields = ('id', 'text', 'product', 'stars')


class ProductReviewSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    reviews = ReviewSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category', 'reviews', 'rating')

    def get_rating(self, obj):
        sum_stars = sum(review.stars for review in obj.reviews.all())
        count_reviews = obj.reviews.count()
        if count_reviews > 0:
            return sum_stars / count_reviews
        else:
            return 0.0
