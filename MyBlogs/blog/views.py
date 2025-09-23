from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404


# Create your views here.


def home(request):
    #load all the post from db
    posts = Post.objects.all()[:11]
    # print(posts)
    cats = Category.objects.all()
    data = {
        'posts': posts,
        'cats': cats,
    }
    return render(request, 'home.html',data)

from django.shortcuts import get_object_or_404

def post(request, url):
    print("DEBUG: url param is:", url)
    post_obj = get_object_or_404(Post, url=url)
    print("DEBUG: post found:", post_obj.title, post_obj.cat, post_obj.image)
    cats = Category.objects.all()
    return render(request, 'posts.html', {'post': post_obj, 'cats': cats})

# def post(request, url):
#     post = Post.objects.filter(url = url)
#     cats = Category.objects.all()
#     print(post)
#     return render(request,'posts.html',{'post':post,'cats':cats})

def category(request, url):
    cat = Category.objects.get(url =url)
    posts = Post.objects.filter(cat=cat)
    return render(request,'category.html', {'cat':cat,'posts':posts})

def about(request):
    return render(request,'about.html')