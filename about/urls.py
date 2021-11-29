from django.urls import path
from .views import aboutt

app_name = 'about'

urlpatterns = [
    path('acercade/', aboutt, name="about")
]