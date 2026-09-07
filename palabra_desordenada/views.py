import random, getpass

from django.shortcuts import render, redirect
from .models import Palabra
from .forms import PalabraForm
#from django.contrib import messages
from .context_processors import respuesta
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required

contador = 0

def manual (request):
    palabra_desordenada="......"
    if request.method == 'POST':
        #ordenada = getpass.getpass("ingresar palabra ")
        #ordenada=ordenada.upper()
        ordenada=request.POST.get("palabra")
        ordenada=ordenada.lower()
        cant_letras = len(ordenada)
        if cant_letras == 2 or cant_letras == 3:
            if ordenada[0] == ordenada[1]:
                return render(request, "registar_palabra.html",{'form':"Ah no eh!"})
        elif cant_letras == 4 or cant_letras == 5:
            if ordenada[0] == ordenada[1] and ordenada[1] == ordenada[2]:
                return render(request, "registar_palabra.html",{'form':"Ah no eh!"})        
        else:
            if ordenada[0] == ordenada[1] and ordenada[1] == ordenada[2] and ordenada[3] == ordenada[4]:
                return render(request, "registar_palabra.html",{'form':"Ah no eh!"})
        desordenada=[]
        for x in ordenada:
            desordenada.append(x)
        random.shuffle(desordenada)
        d="".join(desordenada)
        while d == ordenada:
            desordenada=list(d)
            random.shuffle(desordenada)
            d="".join(desordenada)
        palabra_desordenada = d.upper()

    return render(request, "manual.html",{'palabra_desordenada':palabra_desordenada})

def automatico (request):
    palabra_desordenada="......"
    respuesta="......"
    iden=0
    if request.method == 'POST':
        cantidad_registros = Palabra.objects.count()
        id = random.randint(1, cantidad_registros)
        form=Palabra.objects.get(id=id)
        desordenada=[]
        palabra=form.palabra
        respuesta=palabra
        iden=form.id
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

@login_required
def crear_registro(request):
    x=0
    if request.method == "POST":
        palabra=request.POST.get("palabra")
        palabra=palabra.lower()
        cant_letras = len(palabra)
        if cant_letras == 2 or cant_letras == 3:
            if palabra[0] == palabra[1]:
                return render(request, "registar_palabra.html",{'form':"Ah no eh!"})
        elif cant_letras == 4 or cant_letras == 5:
            if palabra[0] == palabra[1] and palabra[1] == palabra[2]:
                return render(request, "registar_palabra.html",{'form':"Ah no eh!"})        
        else:
            if palabra[0] == palabra[1] and palabra[1] == palabra[2] and palabra[3] == palabra[4]:
                return render(request, "registar_palabra.html",{'form':"Ah no eh!"})
            
        #if palabra[5] == palabra[4] and palabra[4] == palabra[3] and palabra[2] == palabra[1] and palabra[1] == palabra[0]:
        #    return render(request, "registar_palabra.html",{'form':"Ah no eh!"})
        form=PalabraForm(request.POST)
        if form.is_valid():
            form.cleaned_data["palabra"]=form.cleaned_data["palabra"].lower()
            form.save()
            #messages.success(request, 'Palabra registrada')
            #return redirect("automatico")
            form=PalabraForm()
            return render(request, "registar_palabra.html", {"form":"Palabra registrada!"})

    else:
        form=PalabraForm()
        return render(request, "registar_palabra.html", {"form":""})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('automatico')

def signout(request):
    logout(request)
    return redirect('automatico')

@login_required
def solucion(request):
    if request.method == "POST":
        id=request.POST.get('solucion')
        try:
            form=Palabra.objects.get(id=id)
        except:
            return render(request, "solucion.html",{"solucion":"No existe en la base de datos"})

        solucion=form.palabra
        return render(request, "solucion.html", {"solucion":solucion})

    else:

        return render(request, "solucion.html")




