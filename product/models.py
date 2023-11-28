from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.IntegerField(default=1, choices=[(i, i * '*') for i in range(1, 6)], null=True)

    def __str__(self):
        return self.text
