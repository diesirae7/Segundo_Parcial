from django.shortcuts import render
from django.http import HttpResponse
from .models import tessiu
import pandas as pd
import math 
# Create your views here.

def home(request):
    lista = tessiu.objects.get_queryset()
    L1,L2 =procesalista(lista)
    template_name='templates/home/home.html'
    mislistas = [lista,L1,L2]
    diccionario={'lista':lista,"otra":"Informaciòn","L1":L1,"L2":L2,"MISLISTAS":mislistas}
    return render(request, template_name, diccionario)

def procesalista(L):
    listaColorMayor20=[]
    listaColorMenor20=[]
    for i in L:
        if i.Color > 20:
            listaColorMayor20.append(i)
        else:
            listaColorMenor20.append(i)

    return listaColorMayor20,listaColorMenor20
    #return HttpResponse('<h1>Hola Mundo</h1><li>Hola</li>')
def procesamiento (request):
    UMBRAL=0
    if request.method == 'GET':
        UMBRAL=int(request.GET.get('umbral'))

    print('me mandaste el ',UMBRAL)
    lista = tessiu.objects.get_queryset()
    # L1,L2 =procesalista(lista)
    elementos=len(lista)
    ca=CalculeDistancias(lista,elementos)
    tabla=conectaGrafo(lista,UMBRAL,elementos)
    template_name='templates/grafo/grafo.html' 
    diccionario={'ca':ca,'tabla':tabla}
    return render(request, template_name, diccionario)

def CalculeDistancias(L,el):
    # df=pd.DataFrame(L)
    # L=[{'r1':j,'r2':i ,'conectado':'si'if math.sqrt((df[j:2:el])**2+(df[i:2:el])**2)<= el else 'no'}for j in range(0,el)for i in range(j+1,el)]
    MatrizDis=[]

    for el in L:
        distancia=math.sqrt(el.Temperatura**2+el.Color**2)
        MatrizDis.append(el)
        
    return MatrizDis
def conectaGrafo(L,Um,el):
    MatrizUm=[]
    for el in L:
        distancia=math.sqrt(el.Temperatura**2+el.Color**2)
        if distancia <= Um :
            MatrizUm.append(el)
    return MatrizUm
