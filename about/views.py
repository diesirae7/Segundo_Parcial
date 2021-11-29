from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aboutt(request):
    resultado =mifuncion(request)
    template_name ='templates/about/about.html'
    # dict={"nombreusuario":resultado, 'edad':20}
    return render(request, template_name, )

def mifuncion(args):
    return 'Giovanny'


    #maneras de imprimir en html
    #return HttpResponse('<h1>About</h1><li>Hola</li>')
    # txtHtml="""
    # <h1>Hola</h1>
    # <li>Donde</li>
    # <li>la fiesta</li>
    # """
    # return HttpResponse(txtHtml)
