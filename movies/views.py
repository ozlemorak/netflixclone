from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')


def profiles(request):

    profiller = Profiles.objects.filter(owner = request.user)

    context = {
        'profiller':profiller
    }

    return render(request, 'browse.html',context)




def createProfile(request):
    form = ProfilForm()

    mevcut_profil_sayisi = Profiles.objects.filter(owner = request.user).count()

    max_profil = 4

    if mevcut_profil_sayisi >= max_profil:
        messages.error(request, "4'ten fazla profil olamaz!")
        return redirect('profiles')

    if request.method == "POST":
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.owner = request.user
            profil.save()
            messages.success(request, "Başarıyla profil oluşturuldu!")
            return redirect('profiles')
    
    context = {
        'form':form
    }

    return render(request, "create.html", context)



def edit_profile(request, profile_id):

    profile = Profiles.objects.get(id = profile_id)

    if request.method == "POST":
        form = ProfilForm(request.POST, request.FILES, instance = profile)

        if form.is_valid():
            form.save()
            return redirect('profiles')
    else:
        form = ProfilForm(instance = profile)

    context = {
        'form': form
    }

    return render(request, 'edit_profile.html', context)





def delete_profile(request, profile_id):

    profile = get_object_or_404(Profiles, id = profile_id)

    if request.method == "POST":
        profile.delete()
        messages.success(request, "Profil silindi!")
        return redirect('profiles')
    
    context = {
        'profile':profile
    }

    return render(request, 'delete_profile.html',context)



def movies(request):

    filmler = Movie.objects.all()
    user = request.user.kullanici

    context = {
        'filmler' : filmler,
        'user': user
    }

    return render(request, 'browse-index.html', context)


def videos(request, videoAdi):

    videolar = Movie.objects.filter(isim=videoAdi)

    context = {
        'videolar':videolar
    }

    return render(request, 'video.html', context)