#access database, create/delete users, delete polls

from django.contrib import admin
from .models import Album, Song



#tells django that album as admin interface
#makes album table appear on site
admin.site.register(Album)

#whenever we add songs, we can manage them here in the admin panel
admin.site.register(Song)