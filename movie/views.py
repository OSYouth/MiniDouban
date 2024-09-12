from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def moviehome(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'moviehome.html', {'searchTerm':searchTerm})

def home(request):
    return render(request, 'home.html', {'name':'OSYouth'})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})
