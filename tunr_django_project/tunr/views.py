from django.shortcuts import render

from .models import Artist, Song
# Create your views here.

def artist_list(request):
    #using the model to grab all the artists and save
    # in the variable artists
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})



