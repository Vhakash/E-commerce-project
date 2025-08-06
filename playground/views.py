from django.shortcuts import render
from django.http import HttpResponse

#it takes a request and returns a response
# request handlers are functions that take a request and return a response
# Create your views here.

def say_hello(request):
    return HttpResponse("Hello, world! This is the playground app.")