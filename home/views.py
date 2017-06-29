from django.shortcuts import render



def index(request):
    return render(request, 'home/index.html')


def contacto(request):
    contacto = "Diego Barriga"
    direction_list = ["Calle Olmos", "Fray Jose Mujica", "Calle 5 de Mayo", "Just another direccion"]
    administradores = [
        {'nombre': "Juan Pedro", 'apellidos': "Salazar Torres", 'email': "un_correo@gmail.com", 'encargado': True},
        {'nombre': "San Diego", 'apellidos': "Barrios Campos", 'email': "un_correo2@gmail.com", 'encargado': False},
        {'nombre': "Paloma ", 'apellidos': "Limon Bello", 'email': "un_correo3@gmail.com", 'encargado': False}
    ]
    return render(request, "home/contacto.html", {'contacto': contacto, 'direcciones': direction_list, 'admins': administradores})
