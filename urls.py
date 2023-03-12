from django.urls import path
from . import views



urlpatterns = [
   
    path('', views.Post, name='Post'),
    path('detail/<int:pk>', views.detail, name='detail'),
]