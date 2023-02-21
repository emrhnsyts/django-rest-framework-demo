from django.urls import path

from comments.views import CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('',CommentListCreateAPIView.as_view(),name='comment-list'),
    path('<int:pk>/',CommentRetrieveUpdateDestroyAPIView.as_view(),name='comment-detail')
]