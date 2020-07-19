from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Details
from .forms import albumForm, DetailForm

# Create your views here.
def index(request):
  all_albums = Album.objects.all()
  return render(request, 'albums/list_albums.html', context={'albums':all_albums})

def add_albums(request):
    if request.method == 'GET':
        form = albumForm()
    else:
        form = albumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_albums.html", {"form": form})

def delete_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='index')
    return render(request, "albums/delete_albums.html", context={"albums": album})

def albums_detail(request, pk):
  albums = get_object_or_404(Album, pk=pk)
  return render(request, "albums/albums_detail.html", {"albums": albums})

def add_details(request, pk):
    albums = get_object_or_404(Album, pk=pk)

    if request.method == 'GET':
        form = DetailForm()
    else:
        form = DetailForm(data=request.POST)
        if form.is_valid():
            new_details = form.save(commit=False)
            new_details.albums = albums
            new_details.save()
            return redirect(to='list_albums', pk=pk)

    return render(request, "albums/add_details.html", {"form": form, "albums": albums})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = DetailForm(instance=album)
    else:
        form = DetailForm(data=request.POST, instance=album)

        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
            
    return render(request, "albums/edit_albums.html", {
        "form": form,
        "album": album
    })




# from django.db import models
# # Create your models here.
# class Album(models.Model):
#     artist = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     released = models.DateField()
#     image_url = models.TextField(null=True, blank=True)
#     def __str__(self):
#       return f"{self.title} by {self.artist}"
# class Users(models.Model):
#   pass
# class Details(models.Model):
#   detail = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="details")
#   text = models.TextField(null=True, blank=True)
#   date_added = models.DateTimeField(auto_now_add=True)
#   def __str__(self):
#     return f"{self.text}"




# # from django.shortcuts import render,redirect,get_object_or_404
# # from .models import Album
# # from .forms import albumForm

# # # Create your views here.
# # def index(request):
# #   all_albums = Album.objects.all()
# #   return render(request, 'albums/list_album.html', context={'albums': all_albums})

# # def add_album(request):
# #     if request.method == 'GET':
# #         form = AlbumForm()
# #     else:
# #         form = AlbumForm(data=request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect(to='list_album')

# #     return render(request, "albums/add_album.html", {"form": form})

# # def edit_album(request, pk):
# #     album = get_object_or_404(Album, pk=pk)
# #     if request.method == 'GET':
# #         form = AlbumForm(instance=Album)
# #     else:
# #         form= AlbumForm(data=request.POST,instance=album)
# #         if form.is_valid():
# #             form.save()
# #             return redirect(to='list_album')

# #     return render(request, "albums/edit_album.html", {
# #         "form": form,
# #         "album": album
# #     })

# # def delete_album(request, pk):
# #     album = get_object_or_404(Album, pk=pk)
# #     if request.method == 'POST':
# #         album.delete()
# #         return redirect(to='list_album')

# #     return render(request, "albums/delete_album.html", context={"album": album})