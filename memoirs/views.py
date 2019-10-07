from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, Location, Category

def home(request):
    return render(request, 'index.html')


def travel(request):
    render(request, 'travel.html')

def cuisine(request):
    render(request, 'cuisine.html')

def family(request):
    render(request, 'family.html')

def search_results(request):
    if "image" in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_images = Image.search_by_name(search_term)

        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})