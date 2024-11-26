from django.shortcuts import render

class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        super().__init__()


# Create your views here.
def index(request):
    persona1 = Persona("Enzo", "21", "999999999")
    lista = {"barbero1","barbero2","barbero3"}
    contexto = {"nombre" : "Jeffry farias", "barberos": lista, "persona":persona1}
    return render(request, 'barberos/index.html', contexto)

def inicio(request):
    return render(request,'barberos/iniciosesion.html')

def registro(request):
    return render(request,'barberos/registro.html')

def barbero(request):
    return render(request,'barberos/barberos.html')

    