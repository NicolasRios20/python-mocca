from django.shortcuts import redirect, render
from .models import Experiencia, Servicios
# Create your views here.

def blog(request):
    return redirect('/blog/')

def inicio(request):
    experiencias = Experiencia.objects.all()
    servicios = Servicios.objects.all()
    for servicio in servicios:
        descripcion = f"Nuestro servicio de transporte turístico, con capacidad para {servicio.capacidad} pasajeros, ofrece un viaje cómodo y agradable."
        if servicio.aire_acondicionado:
            descripcion += " Equipado con aire acondicionado, garantizamos una atmósfera fresca y confortable sin importar el clima exterior."
        else:
            descripcion += " Sin aire acondicionado, buscamos proporcionar un ambiente confortable a través de una ventilación adecuada."
        
        if servicio.reclinable:
            descripcion += " Las sillas reclinables están diseñadas ergonómicamente para proporcionar el máximo confort durante todo el trayecto."
        else:
            descripcion += " Aunque las sillas no son reclinables, están diseñadas ergonómicamente para proporcionar el máximo confort durante todo el trayecto."
    
        servicio.descripcion_completa = descripcion
    return render(request, 'blog.html' , {'experiencias' : experiencias, 'servicios' : servicios})