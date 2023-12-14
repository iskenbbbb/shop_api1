from rest_framework import serializers

from product.models import Category, Product, Review, Tag


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CategorySerializers(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category

        fields = ('id', 'name', 'product_count')

    @staticmethod
    def get_product_count(obj):
        return obj.products.count()


class ProductSerializers(serializers.ModelSerializer):

    tags = TagSerializers(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category', 'tags')


class ProductValidateSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category', 'tags')
        extra_kwargs = {'tags': {'read_only': True}}

    def validate_tags(self, value: list):
        for tag_id in value:
            try:
                Tag.objects.get(id=tag_id)
            except Tag.DoesNotExist:
                raise serializers.ValidationError(f'Тег с id {tag_id} не найден!')
        return value


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

    @staticmethod
    def get_rating(obj):
        sum_stars = sum(review.stars for review in obj.reviews.all())
        count_reviews = obj.reviews.count()
        if count_reviews > 0:
            return sum_stars / count_reviews
        else:
            return 0.0
