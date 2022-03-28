from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Avatar_of_choice
from .forms import psw_ch

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
    form = psw_ch(response.user)
    cont = {
        'big_username' : response.user.username,
        'form':form,
    }

    if response.method == "POST":
        form = psw_ch(response.user, response.POST)
        if form.is_valid():
            form.save()

    return render(response, 'main/lk.html', cont)    

@login_required
def redactor(request):
    av = Avatar_of_choice.objects.get(usr = User.objects.get(username = request.user.username))
    cont = {
        'username' : request.user.username,
        'avatar' : av,
    }
    return render(request, 'main/list.html', cont)

