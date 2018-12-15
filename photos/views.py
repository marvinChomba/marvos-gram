from django.shortcuts import render,redirect
from .models import Image,Follow,Comments,Profile,idss
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

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
            print(False)
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
        print("Deleted")
        followed = 0
    else:
        Follow.objects.create(user = user, followed_by = request.user)
        print("Created")
        followed = 1
    data = {"hey":"hey", "followed":followed}
    return JsonResponse(data)
