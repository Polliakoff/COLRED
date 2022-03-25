from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Clr_Rgister_Form

# Create your views here.
def register(response):
    if response.method == "POST":
        form = Clr_Rgister_Form(response.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = Clr_Rgister_Form()

    return render(response, 'usr_auth/register.html', {'form':form})