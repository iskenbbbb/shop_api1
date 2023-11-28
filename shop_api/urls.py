from django.urls import path

from product.views import product_list_api_view, reviews_list_api_view, category_list_api_view, product_detail_api_view, \
    category_detail_api_view, reviews_detail_api_view, product_reviews_list_api_view

urlpatterns = [
    path('product/', product_list_api_view),
    path('category/', category_list_api_view),
    path('reviews/', reviews_list_api_view),
    path('product/<int:id>/', product_detail_api_view),
    path('category/<int:id>/', category_detail_api_view),
    path('reviews/<int:id>/', reviews_detail_api_view),
    path('product/reviews/', product_reviews_list_api_view)
]
