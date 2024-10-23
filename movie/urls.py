from django.urls import path
from . import views

urlpatterns = [
    path("moviehome", views.moviehome, name='moviehome'),
    path('<int:movie_id>', views.moviedetail, name='moviedetail'),
]