from django.shortcuts import render,redirect
from .models import Image,Follow,Comments,Profile,idss
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
    image_id = request.POST.get("id")
    if image_id != None:
        idss.objects.create(identifier = request.POST.get("id"))
    last_one = idss.objects.all()
    mwisho = idss.objects.get(pk = last_one.count())
    image = Image.objects.get(pk = mwisho.identifier)
    print(image.likes.all())
    if user in image.likes.all():
        image.likes.remove(user)
    else:
        image.likes.add(user)
    likes = image.likes.all().count()
    data = {"likes":likes}
    return JsonResponse(data)

def comment(request):
    image_id = request.POST.get("id")
    image = Image.objects.get(pk = image_id)
    Comments.objects.create(user = request.user, image = image, comm = request.POST.get("comment"))
    print(request.POST.get("comment"))
    print("*****")
    print(request.POST.get("id"))
    html = render_to_string("comment.html",{"comments":Comments.objects.all()})

    data = {"html":html}

    return JsonResponse(data)