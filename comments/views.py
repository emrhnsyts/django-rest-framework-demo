from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer, CommentSerializerWithoutProductId
from rest_framework.response import Response
from .permissions import IsReadOnlyOrObjectOwner

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReadOnlyOrObjectOwner]
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CommentSerializerWithoutProductId
        return CommentSerializer


