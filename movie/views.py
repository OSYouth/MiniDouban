from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def moviehome(request):
    return HttpResponse('<h1>欢迎来到movie应用首页</h1>')

def home(request):
    return HttpResponse('<h1>欢迎来到项目首页</h1>')