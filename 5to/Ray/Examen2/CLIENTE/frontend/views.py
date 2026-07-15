from django.shortcuts import redirect, render
import requests
from django.views import generic  

# VISTA INDEX

class Index(generic.View):
    template_name = 'home/list_servicios.html'
    context = {}
    url_base = "http://127.0.0.1:8001/cloudsafe_api/api/services/"
    response = None

    def get(self, request):
        self.response = requests.get(url=self.url_base).json()
        self.context = {
            "servicios" : self.response
        }
        return render(request, self.template_name, self.context)
    

class ListServiciosApiView(generic.View):
    template_name = 'home/list_servicios.html'
    context = {}
    url_base = "http://127.0.0.1:8001/cloudsafe_api/api/services/"
    response = None

    def get(self, request):
        self.response = requests.get(url=self.url_base).json()
        self.context = {
            "servicios" : self.response
        }
        return render(request, self.template_name, self.context)


class DetailServicioApiView(generic.View):
    template_name = 'home/detail_servicio.html'
    context = {}
    url_base = "http://127.0.0.1:8001/cloudsafe_api/api/services/"
    response = None

    def get(self, request, pk):
        self.response = requests.get(url=f"{self.url_base}{pk}").json()
        self.context = {
            "servicio" : self.response
        }
        return render(request, self.template_name, self.context)
    

class CreateServicioView(generic.View):
    template_name = 'home/create_servicio.html'
    context = {}
    url_base = "http://127.0.0.1:8001/cloudsafe_api/api/services/create/"
    response = None
    payload = {}

    def get(self, request):
        self.context = {}  
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        self.payload = {
            "nombre": request.POST.get("nombre"),
            "descripcion": request.POST.get("descripcion")
        }
        self.response = requests.post(url=self.url_base, json=self.payload).json()
        return redirect("home:list_servicio")


class UpdateServicioView(generic.View):
    template_name = 'home/update_servicio.html'
    context = {}
    url_get = "http://127.0.0.1:8001/cloudsafe_api/api/services/" 
    url_put = "http://127.0.0.1:8001/cloudsafe_api/api/services/update/"  
    response = None
    payload = {}

    def get(self, request, pk):
        self.response = requests.get(url=f"{self.url_get}{pk}/").json()
        self.context = {
            "servicio": self.response
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request, pk):
        self.payload = {
            "nombre": request.POST.get("nombre"),
            "capacidad": request.POST.get("capacidad"),
            "costo": request.POST.get("costo"),
            "estado": True if request.POST.get("estado") else False
        }
        url_final = f"{self.url_put}{pk}/"
        self.response = requests.put(url=url_final, json=self.payload)
        return redirect("home:list_servicio")
    

class DeleteServicioView(generic.View):
    template_name = 'home/delete_servicio.html'
    url_detail = "http://127.0.0.1:8001/cloudsafe_api/api/services/" 
    url_delete = "http://127.0.0.1:8001/cloudsafe_api/api/services/delete/"

    def get(self, request, pk):
        response = requests.get(url=f"{self.url_detail}{pk}/").json()
        context = {
            "servicio": response
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        url_final = f"{self.url_delete}{pk}/"
        requests.delete(url=url_final)
        return redirect("home:list_servicio")