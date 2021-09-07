import datetime as dt

from django.http import HttpResponse
from django.shortcuts import render

from .models import Category, Image, Location


# Create your views here.
def index(request):

    return render(request, 'index.html',)




def home(request):
    images = Image.objects.all()
    return render(request, 'welcome.html',{'images':images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        
        return render(request, 'all-pics/search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
    return render(request, 'all-pics/search.html',{"message":message})

def location_images(request, location):
    '''
    Function to display images per location
    '''
    location_images = Image.filter_by_location(location)

    return render(request, 'location.html', {"location_images": location_images, "location":location})