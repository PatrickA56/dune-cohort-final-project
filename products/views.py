from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm 
import json

from django.http import JsonResponse, HttpResponse 
from .models import Product, Category 
from django.db.models import Count
from django.contrib import messages

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
 
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer 
from .pagination import ProductPagination
from rest_framework.generics import ListAPIView

from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter


def home(request):
    """Home page view"""
    recent_products = Product.objects.all().order_by('-created_at')[:6]
    categories = Category.objects.all()
    context = {
        'recent_products': recent_products,
        'categories': categories,
    }
    return render(request, 'home.html', context)

def about(request):
    """About page view"""
    return render(request, 'about.html')

def product_list(request):
    """Display all products"""
    products = Product.objects.all().order_by('-created_at')
    context = {'products': products}
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    """Display single product details"""
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)

def category_list(request):
    """Display all categories with product count"""
    categories = Category.objects.annotate(product_count=Count('products'))
    context = {'categories': categories}
    return render(request, 'products/category_list.html', context)

@login_required 
def product_create(request):
    """Create new product"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})
    
@login_required
def product_update(request, pk):
    """Update existing product"""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

@login_required 
def product_delete(request, pk):
    """Delete product"""
    product = get_object_or_404(Product, pk=pk)
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete products.')
        return redirect('product_list')
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'{product_name} deleted successfully.')
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

def product_list_json(request):
    """JSON endpoint for product list"""
    products = Product.objects.all()
    data = [{'id': p.id, 'name': p.name, 'price': str(p.price), 'stock': p.stock} for p in products]
    return JsonResponse(data, safe=False)

def product_detail_json(request, pk):
    """JSON endpoint for single product"""
    try:
        product = Product.objects.get(pk=pk)
        data = {'id': product.id, 'name': product.name, 'price': str(product.price)}
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

# API Views
class ProductListAPIView(ListAPIView):
    """API view for listing and filtering products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'is_available']
    search_fields = ['name', 'category__name']
    ordering_fields = ['price', 'created_at', 'stock']
    ordering = ['-created_at']

class ProductDetailAPIView(APIView):
    """API view for single product operations"""
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk) 
        except Product.DoesNotExist:
            return None 

    def get(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({'error': 'Not found'}, 
            status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({'error': 'Not found'}, 
            status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({'error': 'Not found'},
            status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductCreateAPIView(APIView):
    """API view for creating products"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
