from movies.movie.models import Movie
from django.urls import path
from .views import MovieList

urlpatterns = [
    path('', name="movie_list", view=MovieList.as_view()),
]
