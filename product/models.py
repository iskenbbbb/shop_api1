from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):

    title = models.CharField(max_length=100, verbose_name='название ПРОДУКТА', null=True)
    description = models.TextField(blank=True, verbose_name='описание ПРОДУКТА', null=True)
    price = models.PositiveIntegerField(verbose_name='цена', null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Review(models.Model):

    text = models.TextField(null=True)
    product = Product
