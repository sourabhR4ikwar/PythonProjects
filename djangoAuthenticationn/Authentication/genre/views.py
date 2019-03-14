from django.shortcuts import render
from django.http import HttpResponse
from .models import Collection, Piece

def index(request):
    all_collection = Collection.objects.all();
    context = {
    "all_collection": all_collection
    }
    return render(request,"genre/genreTemplate.html",context)

# Create your views here.

def details(request, genre_id):
    return HttpResponse("<h1>The Genre Id is "+str(genre_id)+" </h1>")
