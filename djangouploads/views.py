from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import UploadForm

def home(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/home.html',context)
    

def movie(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request,'movies/movie.html',{'movie':movie})
    else:
        raise Http404('Movie does not exist')
    

def upload(request):
    if request.POST:
        form = UploadForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'movies/upload.html',{'form': UploadForm})