"""
URL configuration for Meli project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from palabra_desordenada.views import automatico, manual, crear_registro, signout, signin, solucion
from palabra_desordenada.views_de_a_uno import uno_a_uno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', automatico, name='automatico'),
    path('deauno/', uno_a_uno, name='deauno'),
    path('manual/', manual, name='manual'),
    path('registrar/', crear_registro, name='crear_registro'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('solucion/', solucion, name='solucion'),
    #path('palabra_desordenada/', include('palabra_desordenada.urls'))
]