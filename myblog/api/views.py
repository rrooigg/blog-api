from django.shortcuts import render
from rest_framework import generics, status # shows the UI to perform CRUD operations
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
  queryset = BlogPost.objects.all() # gets all posts that exists
  serializer_class = BlogPostSerializer

  # another method to delete(overriding)
  def delete(self, request, *args, **kwargs):
    BlogPost.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer
  lookup_field = "pk" # primary key = id
