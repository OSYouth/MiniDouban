from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator

def bookhome(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        book_list = Book.objects.filter(title__contains=searchTerm)
    else:
        book_list = Book.objects.all()
    paginator = Paginator(book_list, 15)
    page_number = request.GET.get('page', 1)
    books = paginator.page(page_number)

    return render(request, 'bookhome.html', {'searchTerm':searchTerm, 'books':books})