from django.shortcuts import redirect, render
from django.views import generic
import requests
from home import forms
# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    url_base = "http://127.0.0.1:8001/api/v1/users/list" 

    def get(self, request):
        try:
            res = requests.get(self.url_base)
            res.raise_for_status() 
            users_data = res.json()
        except Exception as e:
            print(f"--- ERROR EN API USUARIOS: {e} ---")
            users_data = [] 

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
    
class CreateBankApiView(generic.View):
    template_name = 'home/create_bank.html'
    context = {}
    url_base = "http://127.0.0.1:8001/api/v1/banks/create/"
    response = None
    payload = {}
    form_class = forms.CreateBankForm  # 1. MÍNIMO: Quitamos los () de aquí

    def get(self, request):
        self.context['form'] = self.form_class()  # 2. MÍNIMO: Metemos el formulario al contexto
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        bank_name = request.POST.get("name")  # 3. MÍNIMO: Cambiado () por .get()
        address = request.POST.get("address")  # 3. MÍNIMO: Cambiado () por .get()
        self.payload = {
            "name": bank_name,
            "address": address
        }
        self.response = requests.post(url=self.url_base, json=self.payload).json()
        self.context = {
            "response" : self.response
        }
        return redirect("home:list_banks")
    
class UpdateBankApiView(generic.View):
    template_name = 'home/update_bank.html'
    context = {}
    url_get = "http://127.0.0.1:8001/api/v1/banks/detail/"
    url_put = "http://127.0.0.1:8001/api/v1/banks/update/"
    response = None
    payload = {}

    def get(self, request, pk):
        self.response = requests.get(url=f"{self.url_get}{pk}").json()
        self.context = {
            "bank" : self.response
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request, pk):
        self.payload = {
            "name" : request.POST.get("name"),
            "address" : request.POST.get("address"),
            # 1. CORREGIDO: Convertimos el checkbox vacío en un False real para que la API no falle
            "status" : True if request.POST.get("status") else False
        }
        
        # 2. CORREGIDO: Tu url_put original no tenía "<int:pk>" escrito, así que el replace fallaba. 
        # Armamos la URL limpia usando f-strings.
        url_final = f"{self.url_put}{pk}"
        
        # 3. CORREGIDO: Le quitamos el ".json()" al final de esta línea.
        self.response = requests.put(url=url_final, json=self.payload)
        
        self.context = {
            "response" : self.response.status_code # Guardamos el código de éxito (ej. 200) para evitar que truene
        }
        return redirect("home:list_banks")
    
class DeleteBankApiView(generic.View):
    template_name = 'home/delete_bank.html'
    # Necesitamos dos URLs: una para ver qué vamos a borrar y otra para ejecutar el borrado
    url_detail = "http://127.0.0.1:8001/api/v1/banks/detail/"
    url_delete = "http://127.0.0.1:8001/api/v1/banks/delete/"

    def get(self, request, pk):
        # 1. Traemos los datos del banco para la pantalla de confirmación
        response = requests.get(url=f"{self.url_detail}{pk}").json()
        context = {
            "bank": response
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        # 2. Disparamos la petición de borrado al backend
        url_final = f"{self.url_delete}{pk}"
        
        # OJO AQUÍ: Usamos requests.delete(), que es el estándar para borrar en APIs REST
        requests.delete(url=url_final)
        
        # 3. Redirigimos a la lista de bancos
        return redirect("home:list_banks")