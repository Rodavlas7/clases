"""
URL configuration for frontend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
"""
URL configuration for frontend project.
"""

from django.contrib import admin
from django.urls import path 
from django.urls import include
from client import views

app_name = "home"

urlpatterns = [

    # Rutas de GPS
    path('gps/list/', views.ListGpsView.as_view(), name='list_gps'),
    path('gps/detail/<int:pk>', views.DetailGpsView.as_view(), name='detail_gps'),
    path('gps/create/', views.CreateGpsView.as_view(), name='create_gps'),

    # Rutas de Camiones
    path('trucks/list/', views.ListTruckView.as_view(), name='list_trucks'),
    path('trucks/detail/<int:pk>', views.DetailTruckView.as_view(), name='detail_truck'),
    path('trucks/create/', views.CreateTruckView.as_view(), name='create_truck'),

    path('admin/', admin.site.urls),
    path('', include('client.urls')),
]