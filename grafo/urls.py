from django.urls import path
from django.urls.conf import path
from .views import generaGrafo,procesamiento
urlpatterns = [

    path('grafo/',generaGrafo, name='grafo'),
    path('procesamiento/',procesamiento, name='procesamiento'),

    # path('procesamiento/',procesamiento, name='procesamiento'),
]