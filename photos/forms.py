from django import forms
from .models import Image,Profile

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','pub_date','likes']

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
    pic = forms.ImageField(label = "Pic")