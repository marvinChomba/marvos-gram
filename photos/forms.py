from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','pub_date','likes']
