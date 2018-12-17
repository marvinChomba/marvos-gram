from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Image(models.Model):
    image_url = models.ImageField(upload_to = 'pics', blank = True)
    name = models.CharField(unique = True,max_length = 31, blank = True)
    caption = models.CharField(max_length = 50, blank = True)
    likes = models.ManyToManyField(User, related_name = "likes", blank = True)
    user = models.ForeignKey(User, related_name = "posts")
    pub_date = models.DateTimeField(auto_now_add = True, blank = True)

    def save_image(self):
        self.save()

    def delete_image(self):
        cls.objects.get(id = self.id).delete()

    def update_caption(self,new_caption):
        self.caption = new_caption
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    pic = models.ImageField(upload_to='pics',blank = True)
    bio = models.CharField(default="Hi!", max_length = 30)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    @classmethod
    def search_user(cls,id):
        profile = Profile.objects.get(id = id)
        profile_user_name = profile.user.username
        return User.objects.filter(username__icontains = profile_user_name)

class Comments(models.Model):
    comm = models.CharField(max_length = 100, blank = True)
    image = models.ForeignKey(Image, related_name = "comments")
    user = models.ForeignKey(User, related_name = "comments")

class Follow(models.Model):
    user = models.ForeignKey(User, related_name = "user_followers")
    followed_by = models.ForeignKey(User, related_name = "user_following")

class idss(models.Model):
    identifier = models.CharField(max_length = 30, null = True)