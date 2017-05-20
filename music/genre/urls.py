from django.conf.urls import include, url
from django.contrib import admin
from genre import views

urlpatterns = [
    # Examples:
    url(r'^$', views.home, name="home"),
    url(r'^/song$', views.add_song, name="add_song"),
    # url(r'^blog/', include('blog.urls')),

]
