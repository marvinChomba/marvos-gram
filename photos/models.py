from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image_url = models.ImageField(upload_to = 'pics')
    name = models.CharField(unique = True,max_length = 31)
    caption = models.CharField(max_length = 50)
    likes = models.ManyToManyField(User, related_name = "likes")
    user = models.ForeignKey(User)

class Profile(models.Model):
    user = models.OneToOneField(User,related_name = "profile")
    bio = models.CharField(max_length = 40)
    pic = models.ImageField(upload_to = 'pics')

class Comments(models.Model):
    image = models.ForeignKey(Image, related_name = "comments")
    user = models.ForeignKey(User, related_name = "comments")

class Follow(models.Model):
    user = models.ForeignKey(User, related_name = "followers")
    followed_by = models.ForeignKey(User, related_name = "following")

class idss(models.Model):
    identifier = models.CharField(max_length = 30, null = True)