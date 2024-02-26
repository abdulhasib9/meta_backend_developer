from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World from my app")
def home(request):
    content ="<html><body><h1>Home Page </h1></body></html>"
    return HttpResponse(content)
    