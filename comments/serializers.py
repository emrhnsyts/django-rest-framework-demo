from asyncore import read
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment','evaluation','created_at','product','user']

class CommentSerializerWithoutProductId(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment','evaluation','created_at','user']
    