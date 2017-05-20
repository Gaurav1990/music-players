import os
from django.db import models

RATING = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)

class Genre(models.Model):
    name = models.CharField('name', max_length=256)

    def __unicode__(self):
        return self.name


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    #name = '_'.join(instance.title.split(' '))
    filename = "%s.%s" % (instance.title, ext)
    return os.path.join('/home/vagrant/music_app/music/media/', filename)

class Song(models.Model):
    title = models.CharField('title', max_length=256)
    genre = models.ForeignKey(Genre, verbose_name='Genre Details')
    rating = models.IntegerField('rating', choices = RATING)
    url = models.FileField(upload_to=content_file_name)
    singer = models.CharField('singer', max_length=256)
    composer = models.CharField('composer', max_length=256)
    created_on = models.DateTimeField('provision time', auto_now_add = True)

    def __unicode__(self):
        return self.title
