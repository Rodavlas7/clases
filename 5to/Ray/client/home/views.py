from django.shortcuts import render
from django.views import generic
import requests

# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    context= {}
    url_base = "http://127.0.0.1:8000/api/v1/users/list"
    response = None

    def get(self, request):
        self.response = requests.get(url=self.url_base).json()
        self.context = {
            "users" : self.response
        }
        return render(request, self.template_name, self.context)
