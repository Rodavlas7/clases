from django.urls import path
from client import views

# AQUÍ SÍ FUNCIONA: Esto es lo que repara el error en tus plantillas HTML
app_name = "home"

urlpatterns = [
    # Rutas GPS
    path('gps/list/', views.ListGpsView.as_view(), name='list_gps'),
    path('gps/detail/<int:pk>', views.DetailGpsView.as_view(), name='detail_gps'),
    path('gps/create/', views.CreateGpsView.as_view(), name='create_gps'),

    # Rutas Camiones
    path('trucks/list/', views.ListTruckView.as_view(), name='list_trucks'),
    path('trucks/detail/<int:pk>', views.DetailTruckView.as_view(), name='detail_truck'),
    path('trucks/create/', views.CreateTruckView.as_view(), name='create_truck'),
]