import numpy as np
from django.http import request
from django.shortcuts import render
from home.models import tessiu
import math
# Create your views here.


def generaGrafo(request):
    lista = tessiu.objects.get_queryset()
    template_name='templates/grafo/grafo.html'
    diccionario={}
    calcula(lista)
    return render(request, template_name, diccionario)

def calcula (L):
    n=np.array([1,2,3])
    return n
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

# request es la peticion desde el navegador   
# def procesamiento (request):
#     print("Hola")
