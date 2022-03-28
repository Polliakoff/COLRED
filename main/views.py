from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Avatar_of_choice

@login_required
def main(request):
    av = Avatar_of_choice.objects.get(usr = User.objects.get(username = request.user.username))
    cont = {
        'username' : request.user.username,
        'avatar' : av,
    }
    return render(request, 'main/main_page.html', cont)

@login_required
def lk(request):
    cont = {
        'big_username' : request.user.username,

    }
    return render(request, 'main/lk.html', cont)

