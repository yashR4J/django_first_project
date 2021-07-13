from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # name for reverse lookup
    path('about/', views.about, name='blog-about'),
]