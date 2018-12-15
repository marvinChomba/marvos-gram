from django.shortcuts import render,redirect
from .models import Image,Follow,Comments,Profile,idss
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import ImageForm

# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    images = Image.objects.all()
    for image in images:
        user = image.user
        followers = user.user_followers.all()
        arr_ = []
        for follower in followers:
            arr_.append(follower.followed_by.id)
        if request.user.id in arr_:
            image.user.is_following = True
        else: 
            image.user.is_following = False
        
        if image.user.id == request.user.id:
            user.me = True
            print("Me")
        else:
            user.me = False
    return render(request,"index.html", {"images":images,"user":request.user})

def like(request):
    user = request.user
    images = Image.objects.all()
    image_id = request.POST.get("id")
    if image_id != None:
        idss.objects.create(identifier = request.POST.get("id"))
    last_one = idss.objects.all()
    mwisho = idss.objects.get(pk = last_one.count())
    image = Image.objects.get(pk = mwisho.identifier)
    to_red = None
    if user in image.likes.all():
        image.likes.remove(user)
        to_red = 0
    else:
        image.likes.add(user)
        to_red = 1
    likes = image.likes.all().count()
    data = {"likes":likes, "to_red": to_red}
    return JsonResponse(data)

def comment(request):
    image_id = request.POST.get("id")
    image = Image.objects.get(pk = image_id)
    Comments.objects.create(user = request.user, image = image, comm = request.POST.get("comment"))
    
    user = request.user.username
    comment = request.POST.get("comment")

    data = {"user":user, "comment":comment}
    return JsonResponse(data)

def follow(request):
    image = Image.objects.get(id = request.POST.get("id"))
    user = image.user
    followed = None
    # followers = user.user_followers.all()
    if Follow.objects.filter(user = user, followed_by = request.user):
        Follow.objects.filter(user = user, followed_by = request.user).delete()
        followed = 0
    else:
        Follow.objects.create(user = user, followed_by = request.user)
        followed = 1
    data = {"hey":"hey", "followed":followed}
    return JsonResponse(data)

def add_image(request):
    user = request.user
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = user
            image.save()
        return redirect("index")
    else:
        form = ImageForm()

    return render(request, "add_image.html", {"form":form})

def profile(request,id):
    user = User.objects.get(id = id)
    return render(request, "profile.html", {"user":user})