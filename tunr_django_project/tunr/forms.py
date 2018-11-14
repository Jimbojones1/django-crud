from django import forms
from .models import Artist, Song

class ArtistForm(forms.ModelForm):
  class Meta:
    model = Artist
    fields = ('name', 'nationality', 'photo_url')

class SongForm(forms.ModelForm):
  class Meta:
    model = Song
    fields = ('artist', 'title', 'album', 'preview_url')
