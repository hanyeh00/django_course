#from django.shortcuts import render
from django.http import HttpResponse

def hi(request):
    return HttpResponse("Hello users")

# Create your views here.
