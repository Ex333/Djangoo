from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post__images/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    published = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(max_length=300)

    def __str__(self):
        return self.title