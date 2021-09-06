import datetime as dt

from django.http import HttpResponse
from django.shortcuts import render

from .models import Category, Image, Location


# Create your views here.
def index(request):

    return render(request,'index.html',)
def home(request):
    title = 'Home'
    date = dt.date.today
    photos = Image.get_all()
    return render(request, 'home.html',
                  {"title": title,
                   "date": date,
                   "photos": photos})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'all-pics/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'all-pics/search.html', {"message": message})

def location_images(request, location):
    '''
    Function to display images per location
    '''
    location_images = Image.filter_by_location(location)

    return render(request, 'location.html', {"location_images": location_images, "location":location})
