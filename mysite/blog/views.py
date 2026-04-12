from django.shortcuts import render
from django.http import HttpResponse
from .models import post

def home(request):
    return HttpResponse('Hello Class')

def about(request):
    context = {
        'my_name': 'Alex',
        'my_hobby': 'cooding'
    }
    return render(request, 'blog/about.html', context)
def contact(request):
    return render(request, 'blog/contact.html')

def post_list(request):
    posts = post.objects.filter(is_published = False).order_by("-created_at")

    context ={
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)