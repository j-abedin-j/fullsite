from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post_list/',views.post_list, name='post_list'),
    path('post/new/', views.post_create, name='post_create'),
]