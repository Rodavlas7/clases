from django.shortcuts import redirect, render
from django.views import generic
import requests

# GPS VIEWS

class ListGpsView(generic.View):
    template_name = 'home/list_gps.html'
    context = {}
    url_base = "http://127.0.0.1:8001/v1/gps/list"
    response = None

    def get(self, request):
        self.response = requests.get(url=self.url_base).json()
        self.context = {
            "gps_list": self.response
        }
        return render(request, self.template_name, self.context)


class DetailGpsView(generic.View):
    template_name = 'home/detail_gps.html'
    context = {}
    url_base = "http://127.0.0.1:8001/v1/gps/detail/"
    response = None

    def get(self, request, pk):
        self.response = requests.get(url=f"{self.url_base}{pk}").json()
        self.context = {
            "gps": self.response
        }
        return render(request, self.template_name, self.context)


class CreateGpsView(generic.View):
    template_name = 'home/create_gps.html'
    context = {}
    url_base = "http://127.0.0.1:8001/v1/gps/create"
    response = None
    payload = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        self.payload = {
            "serial_number": request.POST.get("serial_number"),
            "brand": request.POST.get("brand"),
            "model": request.POST.get("model"),
            "is_active": True if request.POST.get("is_active") else False
        }
        self.response = requests.post(url=self.url_base, json=self.payload).json()
        self.context = {
            "response": self.response
        }
        return redirect("home:list_gps")


# TRUCKS VIEWS

class ListTruckView(generic.View):
    template_name = 'home/list_trucks.html'
    context = {}
    url_base = "http://127.0.0.1:8001/v1/trucks/list"
    response = None

    def get(self, request):
        self.response = requests.get(url=self.url_base).json()
        self.context = {
            "truck_list": self.response
        }
        return render(request, self.template_name, self.context)


class DetailTruckView(generic.View):
    template_name = 'home/detail_truck.html'
    context = {}
    url_base = "http://127.0.0.1:8001/v1/trucks/detail/"
    response = None

    def get(self, request, pk):
        self.response = requests.get(url=f"{self.url_base}{pk}").json()
        self.context = {
            "truck": self.response
        }
        return render(request, self.template_name, self.context)


class CreateTruckView(generic.View):
    template_name = 'home/create_truck.html'
    context = {}
    url_base = "http://127.0.0.1:8001/v1/trucks/create"
    response = None
    payload = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        self.payload = {
            "economic_number": request.POST.get("economic_number"),
            "plates": request.POST.get("plates"),
            "brand": request.POST.get("brand"),
            "is_active": True if request.POST.get("is_active") else False
        }
        self.response = requests.post(url=self.url_base, json=self.payload).json()
        self.context = {
            "response": self.response
        }
        return redirect("home:list_trucks")
    