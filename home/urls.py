from django.urls.conf import path
from .views import home,procesamiento
from . import views
urlpatterns = [
    path('',home, name='home'),
    path('procesamiento/',procesamiento, name='procesamiento'),
    # con el <int:pk>le decimos que a la  pagina necesita un numero de tipo entero para poder avanzar 
]