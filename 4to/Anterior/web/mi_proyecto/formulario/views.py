from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Usuario


def registro(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        clave = request.POST.get("clave")
        genero = request.POST.get("genero")
        comentarios = request.POST.get("comentarios")

        Usuario.objects.create(
            nombre=nombre,
            correo=correo,
            clave=make_password(clave),
            genero=genero,
            comentarios=comentarios
        )

        return redirect("exito")

    return render(request, "index.html")


def exito(request):
    return render(request, "exito.html")
