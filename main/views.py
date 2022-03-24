from django.shortcuts import render

def main(request):
    return render(request, 'main/main_page.html')

def login(request):
    return render(request, 'main/login_page.html')

