from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kullanici(models.Model):
    isim = models.CharField(max_length = 50)
    soyisim = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50, null = True)
    resim = models.FileField(upload_to="kullanicilar/", verbose_name="Kullanıcı Resmi", null=True)
    tel = models.IntegerField(default = 0)
    dogum = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.isim
    