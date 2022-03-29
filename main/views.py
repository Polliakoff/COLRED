from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Avatar_of_choice
from .forms import psw_ch
from django.contrib.auth import update_session_auth_hash

@login_required
def main(request):
    av = Avatar_of_choice.objects.get(usr = User.objects.get(username = request.user.username))
    cont = {
        'username' : request.user.username,
        'avatar' : av,
    }
    return render(request, 'main/main_page.html', cont)

@login_required
def lk(response):
    av = Avatar_of_choice.objects.get(usr = User.objects.get(username = response.user.username))
    if response.method == "POST":
        if response.POST.get('_blank'):
            av.name = 'blank'
            av.save(update_fields = ['name'])
            form = psw_ch(response.user)
        elif response.POST.get('_elf'):
            av.name = 'elf'
            av.save(update_fields = ['name'])
            form = psw_ch(response.user)
        elif response.POST.get('_dwarf'):
            av.name = 'dwarf'
            av.save(update_fields = ['name'])
            form = psw_ch(response.user)
        elif response.POST.get('_cobalt'):
            av.name = 'cobalt'
            av.save(update_fields = ['name'])
            form = psw_ch(response.user)

        else:
            form = psw_ch(response.user, response.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(response, user)
    else:
        form = psw_ch(response.user)

    cont = {
        'big_username' : response.user.username,
        'form':form,
        'avatar' : 'main/images/avatars/'+str(av)+'.png',
    }
    return render(response, 'main/lk.html', cont)    

@login_required
def redactor(request):
    av = Avatar_of_choice.objects.get(usr = User.objects.get(username = request.user.username))
    cont = {
        'username' : request.user.username,
        'avatar' : av,
    }
    return render(request, 'main/list.html', cont)

