from rest_framework import serializers
from .models import Item, ProductCategory, Supplier, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    supplier = serializers.StringRelatedField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Item
        fields = ['sku', 'name', 'category', 'tags', 'quantity', 'price', 'description', 'supplier']
