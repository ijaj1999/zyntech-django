from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title

from django.db import models
from django.utils.text import slugify

from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    benefits = models.TextField(help_text="Separate benefits by comma")  # e.g. "Fast, Secure, Scalable"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Auto-generate slug from title
        super().save(*args, **kwargs)

    def benefits_list(self):
        return self.benefits.split(",")  # Convert string to list

    def __str__(self):
        return self.title