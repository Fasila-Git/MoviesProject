from . import views
from django.urls import path
app_name='movieapp'

urlpatterns = [
    path('',views.index,name="index"),
    path('movie/<int:movie_id>',views.details,name="details"),
    path('addmovie/',views.add_movie,name='addmovies'),
    path('edit/<int:id>/',views.editing,name="edit"),
    path('delete/<int:movie_id>/',views.delete,name="delete"),
]