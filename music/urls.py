#create list of urls , import it on website urls
from django.conf.urls import url
from . import views

#namespace, specifying this detail view with this app/url
#will not conflict with other apps detail view
app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/
    #group urls together, look for id number[0-9], connect with view function
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/2/
    #update
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    #register user
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

]