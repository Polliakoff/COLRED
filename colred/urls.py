
from django.contrib import admin
from django.urls import path, include
from usr_auth import views as v_u

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',v_u.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', include('main.urls')),

]
