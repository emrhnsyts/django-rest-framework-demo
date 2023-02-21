from asyncore import read
from dataclasses import fields
from rest_framework import serializers
from comments.serializers import CommentSerializer, CommentSerializerWithoutProductId
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializerWithoutProductId(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','price','description','created_at','comments']

        