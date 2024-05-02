from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import PasswordChangeForm

from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def userRegister(request):

    # form = UserForm()
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Başarıyla Kayıt Oldunuz!")
    #         return redirect('login')

    # context = {
    #     'form':form
    # }

    if request.method == "POST":
        isim = request.POST['isim']
        soyisim = request.POST['soyisim']
        email = request.POST['email']
        resim = request.FILES['resim']
        tel = request.POST['tel']
        dogum = request.POST['dogum']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if sifre1 == sifre2:
            if User.objects.filter(email = email).exists():
                messages.error(request, "Bu mail zaten kullanılmakta")
                return redirect('register')
            elif len(sifre1)< 8:
                messages.error(request,"Şifre 8 karakterden kısa olamaz!")
                return redirect("register")
            elif '!' in isim or '?' in isim:
                messages.error(request, "İsim özel karakterden oluşamaz.")
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=email, email=email, password=sifre1)

                Kullanici.objects.create(
                    user = user,
                    isim = isim,
                    soyisim = soyisim,
                    email = email,
                    resim = resim,
                    tel = tel,
                    dogum = dogum,
                )

                user.save()
                subject = "29 ocak grubu hk."
                message = "Bu dersi 29 Ocak grubu ile yaptık !"

                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                )


                messages.success(request, "Kullanıcı başarıyla oluşturuldu!")
                return redirect('login')

    return render(request, "register.html")



def userLogin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username , password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Başarıyla Giriş Yaptınız!")
            return redirect('profiles')
        else:
            messages.error(request, "Kullanıcı adı veya şifre hatalı!")
            return redirect('login')

    return render(request, 'login.html')



def userLogout(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yapıldı")
    return redirect('login')


def hesap(request):
    user = request.user.kullanici

    context = {
        'user':user
    }

    return render(request, 'hesap.html', context)



def passwordChange(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            logout(request)
            messages.success(request, "Şifre değiştirme başarılı")
            return redirect('login')
        else:
            messages.error(request, "Başarısız işlem")
    
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form':form
    }

    return render(request, 'password_change.html',context)


def accountDelete(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request,"Hesabınız başarıyla silindi.")
        return redirect("register")
    
    return render(request, "account_delete.html")