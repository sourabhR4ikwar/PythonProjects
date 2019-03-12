from django.shortcuts import render
from django.http import HttpResponse
# /Products
def index(request):
    return HttpResponse("Hello World")
