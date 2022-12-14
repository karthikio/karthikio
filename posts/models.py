from django.db import models
from django.utils.text import slugify


# Tag class 
class Tag(models.Model):
  name = models.CharField(max_length=100, unique=True, null=True)
  image = models.ImageField(blank=True, null=True, upload_to='uploads/tags/')
  slug = models.SlugField(null=True, blank=True)

  def save(self, *args, **kwargs):
    if self.slug is None: 
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return str(self.name)


# Post class
class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  info = models.TextField(null=True, max_length=500)
  image = models.ImageField(blank=True, null=True, upload_to='uploads/images/%Y/%m/')
  body = models.TextField(max_length=5000)
  slug = models.SlugField(null=True, blank=True)
  created = models.DateField(auto_now_add=True, auto_now=False)
  tag = models.ManyToManyField(Tag)

  def save(self, *args, **kwargs):
    if self.slug is None: 
      self.slug = slugify(self.title)
    super().save(*args, **kwargs)

  def __str__(self):
    return str(self.title)

