from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie

from .forms import MovieForm
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,"index.html",context)

def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movies':movie})

def add_movie(request):
    if request.method == 'POST':
        movieName=request.POST.get('title')
        moviedesc = request.POST.get('description')
        movieYear = request.POST.get('year')
        movieImg = request.FILES['image']
        moviesAdded=Movie(name=movieName,desc=moviedesc,year=movieYear,img=movieImg)
        moviesAdded.save()
        return redirect('/')

    return render(request,'add.html')

def editing(request,id):
    movie_id=Movie.objects.get(id=id)
    movie_form=MovieForm(request.POST or None,request.FILES, instance=movie_id)
    if movie_form.is_valid():
        movie_form.save()
        return redirect('/')

    return render(request,"edit.html",{'form':movie_form, 'id':movie_id})

def delete(request,movie_id):
    if request.method=='POST':
        movieId=Movie.objects.get(id=movie_id)
        movieId.delete()
        print("deleted")
        return redirect('/')
    return render(request,"delete.html")

