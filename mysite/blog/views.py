from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import post
from .forms import PostForm

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    context = {
        'my_name': 'Alex',
        'my_hobby': 'cooding'
    }
    return render(request, 'blog/about.html', context)
def contact(request):
    return render(request, 'blog/contact.html')

def post_list(request):
    posts = post.objects.filter(is_published = True).order_by("-created_at")

    context ={
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})