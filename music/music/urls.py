from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from genre import urls as genre_urls
from genre import views
urlpatterns = [
    # Examples:
    url(r'^$', views.home, name="home"),
#    url(r'^$', include(genre_urls)),
    url(r'^add/song$', views.add_song, name="add_song"),
    url(r'^add/genre$', views.add_genre, name="add_genre"),
    url(r'^edit/genre/(?P<genre_id>[0-9]+)$', views.edit_genre, name="edit_genre"),
#    url(r'^add/$', include(genre_urls)),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
]
