from django.shortcuts import render
from django.http import HttpResponse

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