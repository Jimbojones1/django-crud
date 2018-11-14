from django.shortcuts import render, redirect

from .models import Artist, Song
from .forms import ArtistForm, SongForm

############################### ARTIST ###############################

# Artist Index
def artist_list(request):
  artists = Artist.objects.all()
  return render(request, 'tunr/artist_list.html', {'artists': artists})

# Artist Show
def artist_detail(request, pk):
  artist = Artist.objects.get(id=pk)
  return render(request, 'tunr/artist_detail.html', {'artist': artist})

# Artist Create
def artist_create(request):
  if request.method == 'POST':
    form = ArtistForm(request.POST)
    if form.is_valid():
      artist = form.save()
      return redirect('artist_detail', pk=artist.pk)
  else:
    form = ArtistForm()
  return render(request, 'tunr/artist_form.html', {'form': form})

# Artist Edit
def artist_edit(request, pk):
  artist = Artist.objects.get(pk=pk)
  if request.method == 'POST':
    form = ArtistForm(request.POST, instance=artist)
    if form.is_valid():
      artist = form.save()
      return redirect('artist_detail', pk=artist.pk)
  else:
    form = ArtistForm(instance=artist)
  return render(request, 'tunr/artist_form.html', {'form': form})

# Artist Delete
def artist_delete(request, pk):
  Artist.objects.get(id=pk).delete()
  return redirect('artist_list')

############################### SONG ###############################

def song_list(request):
  songs = Song.objects.all()
  return render(request, 'tunr/song_list.html', {'songs': songs})

def song_detail(request, id):
  song = Song.objects.get(id=id)
  return render(request, 'tunr/song_detail.html', {'song': song})

# Song Create
def song_create(request):
  if request.method == 'POST':
    form = SongForm(request.POST)
    if form.is_valid():
      song = form.save()
      return redirect('song_detail', id=song.id)
  else:
    form = SongForm()
  return render(request, 'tunr/song_form.html', {'form': form})

  # Song Edit
def song_edit(request, id):
  song = Song.objects.get(id=id)
  if request.method == 'POST':
    form = SongForm(request.POST, instance=song)
    if form.is_valid():
      song = form.save()
      return redirect('song_detail', id=song.id)
  else:
    form = SongForm(instance=song)
  return render(request, 'tunr/song_form.html', {'form': form})

# Song Delete
def song_delete(request, id):
  Song.objects.get(id=id).delete()
  return redirect('song_list')
