from django.db import models

# Create your models here.
class Urun(models.Model):
    isim = models.CharField(max_length=100)
    resim = models.ImageField(upload_to='urun_resimleri/')
    sayi = models.IntegerField()
    fiyat = models.DecimalField(max_digits=8, decimal_places=2)
    kargo_bedeli= models.IntegerField()

def __str__(self):
        return self.isim


class Bakiye(models.Model):
    id = models.IntegerField(primary_key=True)
    bakiyem = models.IntegerField()

def __str__(self):
        return self.id

class kod(models.Model):
    kodum = models.CharField(max_length=1000,default=0)
    
def __str__(self):
        return self.kodum

class kartlar(models.Model):
    numara = models.IntegerField(default=0,null=True)
    isim = models.CharField(max_length=40,default=0,null=True)
    tarih = models.CharField(max_length=6,null=True)
    guvenlik_kodu = models.CharField(max_length=4,null=True);  

def __str__(self):
        return self.numara