import datetime
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    blog_image = models.FileField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.headline

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=555)
    subject = models.CharField(max_length=555)
    email = models.EmailField(max_length=264)
    description = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=200)
    body_text = models.TextField()

    def __str__(self):
        return self.title
