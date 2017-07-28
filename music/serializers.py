from rest_framework import serializers
from .models import Album, Song

#common class naming convention
#needs to inherit serializers
#converting it to JSON, based on model
class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album

        #return only these attributes
        fields = ('artist', 'album_title')

        #or return everything
        #fields = '__all__'