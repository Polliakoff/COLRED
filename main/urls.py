from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('lk',views.lk, name ='lk'),
    path('redactor',views.redactor, name ='redactor'),
]
