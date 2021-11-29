from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def principall(request):
    template_name ='templates/sin/s.html'
    diccionariocontenido={'lista':[1,2,3,4,5]}
    return render(request, template_name, diccionariocontenido)

# def principal(request):
#     return HttpResponse('<h1>Sintactico Estructural</h1><li>Hola</li>')