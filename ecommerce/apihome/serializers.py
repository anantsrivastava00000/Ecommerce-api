from rest_framework import serializers 
from .models import Cateogry, Subcateogry, Product, Color, Ram, Storage, Product_variant, User
from django.contrib.auth.models import User

class Product_variantSerializer(serializers.ModelSerializer): #Song
    class Meta:
        model=Product_variant
        fields=['id', 'product', 'image', 'color', 'price', 'ram', 'storage']
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['product']=Product.objects.filter(id=instance.product.id).values()
            representation['color']=Color.objects.filter(id=instance.color.id).values()
            representation['ram']=Ram.objects.filter(id=instance.ram.id).values()
            representation['storage']=Storage.objects.filter(id=instance.storage.id).values()
            return representation

class ProductvariantSerializer(serializers.ModelSerializer):
    # product=serializers.StringRelatedField(read_only=True)
    # color=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Product_variant
        fields=['id', 'product', 'image', 'color', 'price', 'ram', 'storage']

class ProductSerializer(serializers.ModelSerializer):
    product_variant=ProductvariantSerializer(read_only=True, many=True)
    class Meta:
        model=Product
        fields=['id', 'name', 'subcateogry', 'product_variant'] 

 

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id', 'name', 'subcateogry']


class ProductsvariantSerializer(serializers.ModelSerializer): #Song
    product=ProductsSerializer(read_only=True)
    class Meta:
        model=Product_variant
        fields=['id', 'product', 'image', 'color', 'price', 'ram', 'storage']
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['color']=Color.objects.filter(id=instance.color.id).values()
            representation['ram']=Ram.objects.filter(id=instance.ram.id).values()
            representation['storage']=Storage.objects.filter(id=instance.ram.id).values()
            return representation

# # for user in token authentication we need this 
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=[ 'username', 'password']




 

    

