from django.db import models

# Create your models here.

## models.Model inside the parenthesis, this is how inheritance
## works in python
## SO are class is inheriting methods for a model
## Create, Find, delete ### are methods will probably cover all crud actions

class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    preview_url = models.TextField()

    def __str__(self):
        return self.title









