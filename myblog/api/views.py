from django.shortcuts import render
from rest_framework import generics, status # shows the UI to perform CRUD operations
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

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

class BlogPostList(APIView):
  def get(self, request, format=None):
    # get title from the query parameters(if none, default to empty string)
    title = request.query_params.get("title", "")
    
    if title:
      # filter queryset based on title
      blog_posts = BlogPost.objects.filter(title__icontains=title)
    else:
      # if no title is provided, return all blog posts
      blog_posts = BlogPost.objects.all()

    serializer = BlogPostSerializer(blog_posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
