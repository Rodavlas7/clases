from django.urls import path
from . import views

urlpatterns = [
    path("", views.registro, name="registro"),
    path("exito/", views.exito, name="exito"),
]
