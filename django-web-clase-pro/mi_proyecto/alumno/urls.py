from django.urls import path
from .views import lista_alumnos

urlpatterns = [
    path('alumnos/', lista_alumnos, name='lista_alumnos'),
]