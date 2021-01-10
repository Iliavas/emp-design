from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.mail import send_mail

from .models import Post

def intro(req):
    return render(req, "first.html", {})


def PostDetails(req, name):
    post = Post.objects.get(title=name)
    print(post.stack)
    ContentList = [{"name": p.descr, "image": p.img} for p in post.stack.all()]
    url = ""
    softUsed = [res for res in post.resources.all()]
    if post.video:
        url = "https://www.youtube.com/embed/"+post.video.split('=')[-1]
    return render(req, "PostDetail.html", {"post": post, "stack": ContentList, "url": url, "softUsed": softUsed})

def get_all_posts(req):
    posts = Post.objects.all()
    return render(req, "Posts.html", {"posts": posts})

def index(req):
    return render(req, "index.html", {})


def what_you_need(req):
    return render(req, "what-do-you-need.html", {})


def contact_us(req, type):
    return render(req, "contact-us.html", {"type": type})


def contact_us_req(req):
    print(req.POST.values)
    send_mail(
        req.POST.get("email", ""),
        req.POST.get("name", "") + " " + req.POST.get("surname", "") + " with phone " +
            req.POST.get("phone", "") + " sending you a message " + req.POST.get("message", ""),
        "il.vsl0110@gmail.com",
        ["empiredesign001@gmail.com"]
    )
    return redirect("index")


def about(req):
    return render(req, "about.html", {})