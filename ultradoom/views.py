from django.shortcuts import render
from .models import *

# Create your views here.
def ultradoom(request):
    videos = Video.objects.all()
    return render(request, 'ultradoom/ultradoom.html',{
          'videos': videos,
          
     })
def upload(request):
    if request.method == "POST":
        Video.objects.create (
            title = request.POST['title'],
            embed = request.POST['embed']
            )

    return render(request, 'ultradoom/upload.html')                 