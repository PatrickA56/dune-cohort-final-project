from django.urls import path 
from . import views 
from .views import ProductListAPIView, ProductDetailAPIView
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('api/products/', ProductListAPIView.as_view(), name='api-product-list'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='api-product-detail'),
    path('api/token/', obtain_auth_token, name='api-token'),
    path('api/token/jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


