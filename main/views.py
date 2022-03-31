from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Avatar_of_choice
from .forms import psw_ch
from .forms import Great_List_Form
from django.contrib.auth import update_session_auth_hash
from .models import Character

@login_required
def main(request):
    av = request.user.chosen_avatar
    chrctrs = request.user.character_set.all()
    cont = {
        'username' : request.user.username,
        'avatar' : av,
        'characters': chrctrs,
    }
    return render(request, 'main/main_page.html', cont)

@login_required
def lk(response):
    av = response.user.chosen_avatar
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
    av = request.user.chosen_avatar
    current_character = Character.objects.get(name = 'GHGHGHGHG')
    
    if request.method == 'POST':
        sent_form = Great_List_Form(request.POST)
        print('IS POST+++++++++++++++++++++++++++++++')
        if sent_form.is_valid():
            print('IS VALID+++++++++++++++++++++++++++++++')
            current_character = sent_form.save()
            #current_character.save()
            return redirect('/redactor')
        print(str(sent_form.errors))
        print(sent_form.non_field_errors)

    form = Great_List_Form(instance=current_character)
    
    cont = {
        'username' : request.user.username,
        'avatar' : av,
        'form' : form,
        'current_character': current_character,
    }
    return render(request, 'main/list.html', cont)

