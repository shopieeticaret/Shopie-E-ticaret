from django.shortcuts import render
from .models import Urun,Bakiye,kartlar
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import JsonResponse


def listeleme(request):
    return render(request, 'listeleme.html')

def sss(request):
    return render(request, 'sss.html')

def form(request):
    return render(request, 'form.html')

def sepet(request):
    bakiye = Bakiye.objects.get(id=1)
    urunler = Urun.objects.all()
    toplam_fiyat = 0
    toplam_kargo_bedeli = 0
    toplam = 0

    for urun in urunler:
     urun.urun_fiyat=(urun.fiyat * urun.sayi) + urun.kargo_bedeli
     toplam_fiyat +=(urun.fiyat * urun.sayi)
     toplam_kargo_bedeli += urun.kargo_bedeli
     toplam = toplam_kargo_bedeli + toplam_fiyat 


    context = {
        'bakiyem': bakiye.bakiyem,
        'urunler': urunler,
        'toplam_fiyat': toplam_fiyat,
        'toplam_kargo_bedeli': toplam_kargo_bedeli,
        'toplam': toplam
    }
    return render(request, 'sepet.html',context)


def odeme(request):
    bakiye = Bakiye.objects.get(id=1)
    urunler = Urun.objects.all()
    kartlarim = kartlar.objects.all()

    toplam_fiyat = 0
    toplam_kargo_bedeli = 0
    toplam = 0

    for urun in urunler:
     toplam_fiyat +=(urun.fiyat * urun.sayi)
     toplam_kargo_bedeli += urun.kargo_bedeli
     toplam = toplam_kargo_bedeli + toplam_fiyat

    context = {
        'bakiyem': bakiye.bakiyem,
        'urunler': urunler,
        'kartlarim': kartlarim,
        'toplam_fiyat': toplam_fiyat,
        'toplam_kargo_bedeli': toplam_kargo_bedeli,
        'toplam': toplam,
        'div2_visible': False,
        'div3_visible': False
    }

    if request.method == 'POST':
     numara = request.POST.get('card-number','')
     isim = request.POST.get('card-name')
     tarih = request.POST.get('expiry-date')
     guvenlik_kodu = request.POST.get('cvv')

    
     existing_kartlar = kartlar.objects.filter(numara=numara)
     if existing_kartlar.exists():
            pass
     else:
            kart_obj = kartlar(isim=isim, numara=numara, tarih=tarih, guvenlik_kodu=guvenlik_kodu)
            kart_obj.save()

    return render(request, 'odeme.html', context)

def Bossepet(request):
    return render(request,'Bossepet.html')

def index(request):
    return render(request, 'index.html')

def tamamlanma(request):
    return render(request,'tamamlanma.html')

def sil(request, isim):
    try:
        urun = Urun.objects.get(isim=isim)
        urun.delete()

        if Urun.objects.exists():
            return redirect('sepet')
        else:
            return redirect('Bossepet')

    except Urun.DoesNotExist:
        return redirect('Bossepet')
    
def kartsil(request, numara):     
    try:
        kartlarim = kartlar.objects.get(numara=numara)
        kartlarim.delete()  
        return redirect('odeme')
    except ObjectDoesNotExist:
        return HttpResponse("Belirtilen numaraya sahip bir kart bulunamadı.")
    
def sepeti_temizle(request):
       Urun.objects.all().delete()
       return redirect('Bossepet')    

def bakiye_ekle(request):
    if request.method == 'POST':
        bakiye_input = int(request.POST.get('bakiye_input'))

        bakiye, _ = Bakiye.objects.get_or_create(id=1)   
        bakiye.bakiyem += bakiye_input  
        bakiye.save()  

        return redirect('odeme')  
    
def bakiyeden_al(request):
        bakiye, _ = Bakiye.objects.get_or_create(id=1) 
        urunler = Urun.objects.all()

        toplam_fiyat = 0
        toplam_kargo_bedeli = 0
        toplam = 0

        for urun in urunler:
         toplam_fiyat +=(urun.fiyat * urun.sayi)
         toplam_kargo_bedeli += urun.kargo_bedeli
         toplam = toplam_kargo_bedeli + toplam_fiyat

        if bakiye.bakiyem < toplam:
         response_data = {
            'bakiye_kontrol': False
         }
        else:
         bakiye.bakiyem -= toplam
         bakiye.save()
         response_data = {
            'bakiye_kontrol': True
        }

        return JsonResponse(response_data)  
