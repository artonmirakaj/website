#blueprint for database, template of how we store data for the app
#django gets each variable from the class and convert it to a column in database
"""
create class
name of variable is column
every class inherits models.Model
to activate models, go to settings, app name.apps.app nameConfig
type path into settings/installed apps
"""
from django.db import models
from django.core.urlresolvers import reverse

#primary key
#name of class is column, has to inherit models.Model
class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    #details page of album that you create
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    #display info. on object(album), objects.get.all()
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)#assocaited with album class
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)#when this is true, song is there favorite

    #display info. on object(album), objects.get.all()
    def __str__(self):
        return self.song_title