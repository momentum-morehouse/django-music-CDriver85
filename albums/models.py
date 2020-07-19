from django.db import models
# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    released = models.DateField()
    image_url = models.TextField(null=True, blank=True)
    def __str__(self):
      return f"{self.title} by {self.artist}"
class Users(models.Model):
  pass
class Details(models.Model):
  detail = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="details")
  text = models.TextField(null=True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f"{self.text}"




# from django.db import models

# # Create your models here.


# class Album(models.Model):

#     artistname = models.CharField(max_length=255)
#     albumtitle = models.CharField(max_length=255)
#     released = models.DateField()
   
    
    
#     def __str__(self):
#       return f"{self.title} by {self.artist}"

# class Users(models.Model):
#   pass

# class Details(models.Model):
#     detail = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="details")
#     text = models.TextField(null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.text}"