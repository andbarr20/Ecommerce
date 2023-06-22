from .models import Department, Municipality, ProductCategory, Product, Profile, Country, Car, CarItem

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
    SerializerMethodField
)
from rest_framework import serializers 


class CategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category_id','name', 'categoryImage', 'description']

class ProductSerializer(ModelSerializer):
    ##productCategory_id = CategorySerializer(many=False)
    class Meta:
        model = Product
        fields = ['name', 'sellPrice','description','productImage']

# class OrdersCreateSerializer(ModelSerializer):
#     class Meta:
#         model = SalesCheck
#         fields = '__all__'

class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# class OrderSerializer(ModelSerializer):
#     class Meta:
#         model = SalesCheck
#         fields = '__all__'

class ShoppingCarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ItemsCarSerializer(ModelSerializer):
    class Meta:
        car = ShoppingCarSerializer(many=False)
        model = CarItem
        fields = '__all__'

class ProductFoodSerializer(ModelSerializer):
    ##productCategory_id = CategorySerializer(many=False)
    class Meta:
        model = Product
        fields = ['name', 'sellPrice','description','productImage']

class ProductFarmacySerializer(ModelSerializer):
    ##productCategory_id = CategorySerializer(many=False)
    class Meta:
        model = Product
        fields = ['name', 'sellPrice','description','productImage']

class ProductToySerializer(ModelSerializer):
    ##productCategory_id = CategorySerializer(many=False)
    class Meta:
        model = Product
        fields = ['name', 'sellPrice','description','productImage']

class ProductSnackSerializer(ModelSerializer):
    ##productCategory_id = CategorySerializer(many=False)
    class Meta:
        model = Product
        fields = ['name', 'sellPrice','description','productImage']