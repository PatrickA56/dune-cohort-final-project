from django.shortcuts import render
from django.http import HttpResponse 


def home(request):
    return HttpResponse('<h1>Welcome to Patakins Mart!</h1>')

def about(request):
    return HttpResponse('<h1>About Us</h1><p>Super Market For Selling And Buying Of Food Stuffs</p>')

def product_list(request):
    return HttpResponse('<h1>Products</h1><p>Here Are Our Products</p>')