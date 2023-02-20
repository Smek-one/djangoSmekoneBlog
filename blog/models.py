from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(upload_to="uploads/", null=True, blank=True)
    content = models.TextField()
    image2 = models.ImageField(upload_to="uploads/", null=True, blank=True)
    image3 = models.ImageField(upload_to="uploads/", null=True, blank=True)
    content2 = models.TextField(blank=True)
    image4 = models.ImageField(upload_to="uploads/", null=True, blank=True)
    image5 = models.ImageField(upload_to="uploads/", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
