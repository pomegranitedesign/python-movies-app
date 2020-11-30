from django.contrib import admin
from django.urls import path, include
from movie import views as movie_views

urlpatterns = [
    path('admin/', name="admin", view=admin.site.urls),
    path('movies/', name="movies", view=movie_views.movie_list)
]
