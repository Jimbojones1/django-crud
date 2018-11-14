from django.shortcuts import render

from .models import Artist, Song
# Create your views here.

def artist_list(request):
    #using the model to grab all the artists and save
    # in the variable artists
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})


### Show Route
def artist_detail(request, pk):
    #pk is short for primary key, basically the id in sql
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})




def song_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs})


### Show Route
def song_detail(request, pk):
    #pk is short for primary key, basically the id in sql
    song = Song.objects.get(id=pk)
    return render(request, 'tunr/song_detail.html', {'song': song})
