from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 1
    y = 2
    return x + y
#it takes a request and returns a response
# request handlers are functions that take a request and return a response
# Create your views here.

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Akash'})