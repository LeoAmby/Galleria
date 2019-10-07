from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')


def travel(request):
    render(request, 'travel.index')

def cuisine(request):
    render(request, 'cuisine.html')

def family(request):
    render(request, 'family.html')