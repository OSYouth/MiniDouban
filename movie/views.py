from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def moviehome(request):
    return render(request, 'moviehome.html')

def home(request):
    return render(request, 'home.html', {'name':'OSYouth'})