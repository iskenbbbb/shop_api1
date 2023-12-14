from django.contrib import admin
from django.urls import path, include
from users import views as user_view
from product import views
urlpatterns = [
    path('product/', views.ProductListAPIView.as_view()),
    path('category/', views.CategoryListAPIView.as_view()),
    path('reviews/', views.ReviewListAPIView.as_view()),
    path('product/<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('category/<int:pk>/', views.CategoryDetailAPIView.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailAPIView.as_view()),
    path('product/reviews/', views.ProductReviewAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('users/register/', user_view.RegisterAPIView.as_view()),
    path('users/login/', user_view.LoginAPIView.as_view()),
    path('users/confirm/', user_view.ConfirmAPIView.as_view()),
]
