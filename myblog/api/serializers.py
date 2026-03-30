# specify a class that converts the model to json compatible data to return and interact with from our api

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPost
    fields = ["id", "title", "content", "published_date"]
