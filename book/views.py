from django.shortcuts import render
from .models import Book

def bookhome(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        books = Book.objects.filter(title__contains=searchTerm)
    else:
        books = Book.objects.all()
    return render(request, 'bookhome.html', {'searchTerm':searchTerm, 'books':books})