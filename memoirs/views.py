from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html')
