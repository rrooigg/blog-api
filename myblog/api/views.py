from django.shortcuts import render
from rest_framework import generics # shows the UI to perform CRUD operations
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
  queryset = BlogPost.objects.all() # gets all posts that exists
  serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer
  lookup_field = "pk" # primary key = id
