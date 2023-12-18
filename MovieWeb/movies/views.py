from django.shortcuts import render
from .models import *

def home(request):
    lasest_trailers = Movie.objects.all().order_by('-id')[:6]
    top_rate = Movie.objects.all().order_by("-rating")[:6]
    top_movies = Movie.objects.annotate(num_comments=models.Count('comments')).order_by('-num_comments')[:6]
    context = {'movies': lasest_trailers, 'rate': top_rate, 'top_movies': top_movies}
    return render(request, 'index.html', context)

def playvideo(request, pk):
    lasest_trailers = Movie.objects.get(id=pk)
    context = {'movies': lasest_trailers}
    return render(request, 'playvideo.html', context)

def playlongvideo(request, pk):
    lasest_film = Movie.objects.get(id=pk)
    context = {'movies': lasest_film}
    return render(request, 'long_video.html', context)

def comment(request, pk):
    movie = Movie.objects.get(id=pk)
    comment = Comment.objects.filter(movie=movie)
    c = len(comment)
    context = {'movies': comment, 'c':c}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("text")
        Comment.objects.create(name=name, email=email, body=text, movie=movie)

    return render(request, 'comment.html', context)

def show_all(request):
    movie = Movie.objects.all()
    context = {
        'movies': movie
    }
    return render(request, 'show_all.html', context)

def search(request):
    if request.method == "GET":
        q = request.GET.get('q')
        search_movies = Movie.objects.filter(name__icontains=q)
        context = {
            'movies': search_movies
        }
    return render(request, 'show_all.html', context)

def error_404(request, exception):
   context = {}
   return render(request,'notfound.html', context)

def error_500(request):
   context = {}
   return render(request,'notfound.html', context)