from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Album
from .forms import UserForm

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlbumSerializer


#lists all albums or create a new one
#albums/
class AlbumList(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self):
        pass


#homepage
class IndexView(generic.ListView):
    #whenever we get our list of albums, plug them into this template
    template_name = 'music/index.html'
    #changes object_list name
    context_object_name = 'all_albums'

    #query database for whatever albums we want
    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    #details for an album
    model = Album
    template_name = 'music/detail.html'


#create a new album
class AlbumCreate(CreateView):
    #the object
    model = Album
    #fields/attributes you need
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    #successfully delete a url, take user back to homepage
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    #blueprint of form
    form_class = UserForm
    #html file that the form is going to be included in
    template_name = 'music/registration_form.html'

    #blank form for user
    def get(self, request):
        # user will fill in data
        form = self.form_class(None)
        #displaying a blank form to user
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #creates object from the form
            user = form.save(commit=False)

            #cleaned (normalized) data/formatted properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #change users password
            user.set_password(password)
            user.save()

            #returns user objects if credentials are correct
            user = authenticate(username=username, password=password)
            #checks in database to see if they are an actual user/exist

            if user is not None:

                #account didnt get banned/
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})