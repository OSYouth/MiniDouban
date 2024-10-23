from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.
def moviehome(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movie_list = Movie.objects.filter(title__contains=searchTerm)
    else:
        movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 15)
    page_number = request.GET.get('page', 1)
    movies = paginator.page(page_number)
    return render(request, 'moviehome.html', {'searchTerm':searchTerm, 'movies':movies})

def home(request):
    return render(request, 'home.html', {'name':'OSYouth'})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def moviedetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'moviedetail.html', {'movie': movie})
