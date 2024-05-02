from django.db import models
from user.forms import *

# Create your models here.
class Profiles(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    isim = models.CharField(max_length = 100)
    resim = models.FileField(upload_to="profiles/", verbose_name="Profil Resmi", null=True)


    def __str__(self):
        return self.isim


class Kategori(models.Model):
    isim = models.CharField(max_length = 50)

    def __str__(self):
        return self.isim
     

class Movie(models.Model):
    isim = models.CharField(max_length = 50)
    resim = models.FileField(upload_to="movieGif/", verbose_name="Film Resmi", null=True)
    video = models.FileField(upload_to="videolar/", verbose_name="Film Videosu", null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.isim
    
    
