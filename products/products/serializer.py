from rest_framework import serializers 
from .models import Product, Category
from products.models import Product 
from products.serializers import ProductSerializer 



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__' 

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), 
    source='category', write_only=True)

    product = Product.objects.first()
    serializer = ProductSerializer(product)
    print(serializer.data)

    data = {'name': 'Apple', 'price': 500, 'stock': 250, 'category_id': 1}
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        product = serilizer.save()
    else:
        print(serializer.errors)