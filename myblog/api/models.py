from django.db import models

# Create your models here.
class BlogPost(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True) # automatically fills this field whenever a blog post is created

  def __str__(self):
    return self.title
