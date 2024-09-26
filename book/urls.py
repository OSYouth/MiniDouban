from django.urls import path
from . import views

urlpatterns = [
    path('bookhome', views.bookhome, name='bookhome'),
]