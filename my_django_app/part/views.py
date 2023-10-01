from django.shortcuts import render
from django.http import HttpResponse

def hello(response):
    return render(response, 'index.html')
# Create your views here.
