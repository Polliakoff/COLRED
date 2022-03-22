from django.shortcuts import render

def main(request):
    return render(request, 'main/footer_base.html')

