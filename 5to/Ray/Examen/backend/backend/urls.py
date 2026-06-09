"""
URL configuration for backend project.

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
from django.urls import path
from api import views

app_name = "api"

urlpatterns = [
    # GPS EndPoints
    path('v1/gps/list', views.ListGpsApiView.as_view(), name="gps_list"),
    path('v1/gps/detail/<int:pk>', views.DetailGpsApiView.as_view(), name="detail_gps"),
    path('v1/gps/create', views.CreateGpsApiView.as_view(), name="create_gps"),

    # Trucks EndPoints
    path('v1/trucks/list', views.ListTruckApiView.as_view(), name="truck_list"),
    path('v1/trucks/detail/<int:pk>', views.DetailTruckApiView.as_view(), name="detail_truck"),
    path('v1/trucks/create', views.CreateTruckApiView.as_view(), name="create_truck"),
]

