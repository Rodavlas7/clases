from django.shortcuts import render
from django.views import generic
import requests

# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    url_base = "http://127.0.0.1:8001/api/v1/users/list" # Asegúrate del puerto

    def get(self, request):
        try:
            res = requests.get(self.url_base)
            # Si no es un 200 OK, esto saltará al except
            res.raise_for_status() 
            users_data = res.json()
        except Exception as e:
            print(f"--- ERROR EN API USUARIOS: {e} ---")
            users_data = [] # Lista vacía para que el template no falle

        context = {
            "users": users_data
        }
        return render(request, self.template_name, context)
    

### BANKS VIEWS

# List and detail BANKS
class ListBankApiView(generic.View):
    template_name = 'home/list_banks.html'
    context = {}
    url_base = "http://127.0.0.1:8001/api/v1/banks/list"
    response = None

    def get(self, request):
        self.response = requests.get(url=self.url_base).json()
        self.context = {
            "banks" : self.response
        }
        return render(request, self.template_name, self.context)


class DetailBankApiView(generic.View):
    template_name = 'home/detail_bank.html'
    context = {}
    url_base = "http://127.0.0.1:8001/api/v1/banks/detail/"
    response = None
    
    def get(self, request, pk):
        self.response = requests.get(url=f"{self.url_base}{pk}").json()
        self.context = {
            "bank" : self.response
        }

        return render(request, self.template_name, self.context)