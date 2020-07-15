from django.shortcuts import render
from .models import Album

# Create your views here.

def index(request):
  all_albums = Album.objects.all()
  return render(request, 'albums/list_album.html', context={'albums': all_albums})
