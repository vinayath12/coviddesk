import requests
from django.shortcuts import render, get_object_or_404
from .models import Place

# Create your views here.
def main(request):

     return render(request,'index.html')
def getplace(request,c_slug=None):
    place=get_object_or_404(Place,slug=c_slug)
    return render(request, 'place.html',{'places':place})

