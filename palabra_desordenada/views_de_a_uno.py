import random
from django.shortcuts import render
from .models import Palabra
from .context_processors import respuesta

contador = 0

def uno_a_uno (request):
    palabra_desordenada="......"
    respuesta="......"
    iden=0
    global contador
    print("ddd")
    if request.method == 'POST':        
        contador = contador + 1
        print(contador)
        cantidad_registros = Palabra.objects.count()
        id=contador
        if id <= cantidad_registros:
        #id = random.randint(contador, cantidad_registros)
            form=Palabra.objects.get(id=id)
            desordenada=[]
            palabra=form.palabra
            respuesta=palabra
            iden=form.id
        else:
            contador = 0
            return render(request, "index.html",{'palabra_desordenada':"De nuevo",'respuesta':respuesta,'iden':iden})
        for x in form.palabra:
            desordenada.append(x)
        random.shuffle(desordenada)
        d="".join(desordenada)
        while d == form.palabra:
            desordenada=list(d)
            random.shuffle(desordenada)
            d="".join(desordenada)
        palabra_desordenada = d.upper()
    return render(request, "index.html",{'palabra_desordenada':palabra_desordenada,'respuesta':respuesta,'iden':iden})