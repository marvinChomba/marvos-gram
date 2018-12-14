from django.shortcuts import render,redirect
from .models import Image,Follow,Comments,Profile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    images = Image.objects.all()
    return render(request,"index.html", {"images":images})

def like(request):
    user = request.user
    images = Image.objects.all()
    id = request.POST.get("id")
    image = Image.objects.get(id = id)
    if user in image.likes.all():
        image.likes.remove(user)
    else:
        image.likes.add(user)
    
    # data = render_to_string("images.html",{"images":images},request)
    likes = image.likes.all().count()
    data = {"likes":likes}
    return JsonResponse(data)