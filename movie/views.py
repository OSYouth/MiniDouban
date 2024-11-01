from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Review
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ReviewForm

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
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'moviedetail.html', {'movie': movie, 'reviews':reviews})

def createmoviereview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET' :
        return render(request, 'createmoviereview.html' ,
        {'form':ReviewForm , 'movie':movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('moviedetail',newReview.movie.id)
        except ValueError:
            return render(request,'createmoviereview.html', {'form':ReviewForm, 'error':'非法数据'})
