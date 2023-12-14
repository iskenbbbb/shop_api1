from django.contrib import admin

from product.models import Product
from product.models import Review
from product.models import Category
from product.models import Tag

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Tag)
