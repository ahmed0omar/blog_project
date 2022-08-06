from django.shortcuts import render, get_object_or_404
from datetime import date
from django.http import Http404
from .models import Post

l=Post.objects.all()
# Create your views here.
def index(request):

    return render(request,"blog/index.html",{"posts":l})
def pData(request,slug):
    post=get_object_or_404(Post,slug=slug)
    return render(request,"blog/pData.html",{"post":post})
def latest_posts(request):
    return render(request,"blog/posts.html",{"posts":l})