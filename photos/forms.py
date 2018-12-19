from django import forms
from .models import Image,Profile
from pyuploadcare.dj.forms import ImageField

class ImageForm(forms.ModelForm):
    image_url = ImageField(label='Picture')
    class Meta:
        model = Image
        fields = ("image_url","name","caption")

# class ImageForm(forms.Form):
#     name = forms.CharField(label = "Name")
#     caption = forms.CharField(label = "Caption")
#     image =forms.ImageField(label = "image")
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ["user"]

class ProfileForm(forms.Form):
    bio = forms.CharField(label = "Bio")
    pic = ImageField(label = "Pic")