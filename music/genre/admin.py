from django.contrib import admin
from genre.models import Song, Genre


# Register your models here.
class AdminSong(admin.ModelAdmin):
    list_display = ('title', 'genre', 'rating', 'singer', 'composer', 'created_on')

# Register your models here.
class AdminGenre(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Song, AdminSong)
admin.site.register(Genre, AdminGenre)