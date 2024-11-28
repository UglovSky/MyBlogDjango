from django.shortcuts import render,get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html' ,{'posts':posts})

def about(request):
    return render(request,'blog/about.html')


def detail(request, post_id):
        posts = get_object_or_404(Post, pk=post_id)
        return render(request, 'blog/detail.html', {'posts': posts})