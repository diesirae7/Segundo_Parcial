from django.urls import path, re_path
from .views import principall

app_name = 'Sintactico'

urlpatterns = [
    path('sin/', principall, name='patrones'),
    path('about/', principall, name='about'),
    path('grafos/', principall, name='grafos'),
    path('home/', principall, name='home'),
]