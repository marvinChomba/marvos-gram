from django.shortcuts import render,redirect
from .models import Image,Follow,Comments,Profile,idss
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import ImageForm,ProfileForm

# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    user_has_liked_list = []
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
        else:
            user.me = False
        if request.user in image.likes.all():
            image.user_has_liked = True
        else:
            image.user_has_liked = False
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

def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new_bio = form.cleaned_data["bio"]
            new_pic = form.cleaned_data["pic"]
            profile = Profile.objects.get(user = request.user)
            profile.bio = new_bio
            profile.pic = new_pic
            profile.save()
            g = "/profile/" + str(request.user.id) + "/"
            return redirect(g)
    else:
        form = ProfileForm()
    return render(request, "update_profile.html", {"form":form})  

def profile(request,id):
    user = User.objects.get(id = id)
    print(request.user.id)
    print("****")
    
    if request.user.id == int(id):
        print("Mine")
        return render(request, "my-profile.html", {"user":user, "current_user":request.user})
    else:
        return render(request, "profile.html", {"user":user,"current_user":request.user})