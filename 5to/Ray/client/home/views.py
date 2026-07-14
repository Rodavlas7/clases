from django.shortcuts import redirect, render
from django.views import generic
import requests
from home import forms
# Create your views here.

class Index(generic.View):
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
    form_class = forms.CreateBankForm 

    def get(self, request):
        self.context['form'] = self.form_class()  
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        bank_name = request.POST.get("name") 
        address = request.POST.get("address")  
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
            "status" : True if request.POST.get("status") else False
        }
        
        url_final = f"{self.url_put}{pk}"
        
        self.response = requests.put(url=url_final, json=self.payload)
        
        self.context = {
        }
        return redirect("home:list_banks")
    
class DeleteBankApiView(generic.View):
    template_name = 'home/delete_bank.html'
    url_detail = "http://127.0.0.1:8001/api/v1/banks/detail/"
    url_delete = "http://127.0.0.1:8001/api/v1/banks/delete/"

    def get(self, request, pk):
        response = requests.get(url=f"{self.url_detail}{pk}").json()
        context = {
            "bank": response
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        url_final = f"{self.url_delete}{pk}"
        requests.delete(url=url_final)
        
        return redirect("home:list_banks")
    
class ListPaymentApiView(generic.View):
    # These are safe as class attributes because they are constants
    template_name = 'home/list_payments.html'
    url_base = "http://127.0.0.1:8001/api/v2/payment/list/"
    url_tc = "http://127.0.0.1:8001/api/v2/tipo_cambio/dolar/pesos"

    def get(self, request):
        # 1. Initialize local variables to avoid state leakage across requests
        payments_data = {}
        tipo_cambio_data = {}
        self.headers = {
            "Authorization": f"Token 1b1594377fcff65694e8a03c86c48b61c3c3de98" if hasattr(request.user, 'auth_token') else ""
        }

        # 2. Safely fetch Payments
        try:
            res_payments = requests.get(url=self.url_base, timeout=5, headers=self.headers)
            res_payments.raise_for_status()
            payments_data = res_payments.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch payments: {e}")

        try:
            res_tc = requests.get(url=self.url_tc, timeout=5)
            res_tc.raise_for_status() 
            tipo_cambio_data = res_tc.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch tipo cambio: {e}")

        context = {
            "payments": payments_data,
            "tipo_cambio": tipo_cambio_data
        }
        
        return render(request, self.template_name, context)
    
class DetailPaymentApiView(generic.View):
    template_name = 'home/detail_payment.html'
    context = {}
    url_base = "http://127.0.0.1:8001/api/v2/payment/detail/"

    def get(self, request, pk):
        self.response = requests.get(url=f"{self.url_base}{pk}").json()
        self.context = {
            "payment": self.response
        }
        return render(request, self.template_name, self.context)

class CreatePaymentApiView(generic.View):
    template_name = 'home/create_payment.html'
    context = {}
    url_create = "http://127.0.0.1:8001/api/v2/payment/create/"
    url_accounts = "http://127.0.0.1:8001/api/v2/account/list/"
    response = None

    def get(self, request):
        self.context['accounts'] = requests.get(url=self.url_accounts).json()
        return render(request, self.template_name, self.context)
    
    
    def post(self, request):
        id_account = [1,2]
        created_by = int(request.POST.get("created_by"))
        name_payload = request.POST.get("name")
        self.payload = {
            "name": name_payload,
            "accounts": id_account,
            "created_by": created_by
        }
        return redirect("home:list_payments")
