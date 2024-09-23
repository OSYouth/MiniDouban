from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def moviehome(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__contains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'moviehome.html', {'searchTerm':searchTerm, 'movies':movies})

def home(request):
    return render(request, 'home.html', {'name':'OSYouth'})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})
