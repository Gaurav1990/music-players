import json
from django.shortcuts import render
from genre.models import Song, Genre
from django.views.decorators.csrf import csrf_exempt
from genre.forms import AddSong, AddGenre
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
@csrf_exempt
def home(request):
    all_songs = Song.objects.all()
    return render(request, 'index.html', locals())

@csrf_exempt
def add_song(request):
    template = 'add_song.html'
    if request.method == 'POST':
        form = AddSong(request.POST, request.FILES)
        if form.is_valid():
            song = Song.objects.create(title = form.cleaned_data['title'],
                                           genre = Genre.objects.get(name = form.cleaned_data['genre']),
                                           url = request.FILES['url'],
                                           rating = form.cleaned_data['rating'],
                                           singer = form.cleaned_data['singer'],
                                           composer = form.cleaned_data['composer'])
            messages.success(request, 'successfully added new song')
            return render(request, 'index.html', locals())
        else:
            return render(request, template, locals())
    else:
        form = AddSong()
        return render(request, template, locals())


@csrf_exempt
def add_genre(request):
    all_genre = Genre.objects.all()
    template = "add_genre.html"
    if request.method == 'POST':
        form = AddGenre(request.POST)
        if form.is_valid():
            genre = Genre.objects.create(name = form.cleaned_data['name'])
            
            messages.success(request, 'successfully added new genre')
            return render(request, 'add_genre.html', locals())
        else:
            return render(request, template, locals())
    else:
        form = AddGenre()
        return render(request, template, locals())

@require_POST
@csrf_exempt
def edit_genre(request, genre_id):
    if request.method == 'POST' and request.is_ajax:
        genre = Genre.objects.get(id = genre_id)
        name = request.POST.get('genre_value')
        genre.name = name
        genre.save()
        return HttpResponse(json.dumps({'resp':'success'}));
    return HttpResponse(json.dumps({'resp':'error'}));