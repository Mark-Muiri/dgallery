from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Category, Location

# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'welcome.html',{'images':images})

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
