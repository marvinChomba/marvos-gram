from django.shortcuts import render,redirect
from .models import Image,Follow,Comments,Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    images = Image.objects.all()
    return render(request,"index.html", {"images":images})

def like(request,id):
    user = request.user
    image = Image.objects.get(id = id)
    if user in image.likes.all():
        image.likes.remove(user)
    else:
        image.likes.add(user)
    return redirect("index")