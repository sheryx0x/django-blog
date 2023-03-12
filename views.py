from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404






def Post(request):
    posts=post.objects.all()
   
    context= {'posts':posts}
    return render(request, 'post.html', context)



def detail(request, pk):
    posts= post.objects.get(id=pk)
   
    context= {'posts':posts}
    return render(request, 'detail_page.html', context)