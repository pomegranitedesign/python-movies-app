from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Movie


def movie_list(request):
    movie_name = request.GET.get('movie_name')
    movies = Movie.objects.all()

    if movie_name != '' and movie_name is not None:
        movies = movies.filter(name__icontains=movie_name)

    paginator = Paginator(movies, 4)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    return render(request, 'movie/movie_list.html', {'movies': movies})
