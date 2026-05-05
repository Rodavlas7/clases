from django.shortcuts import render
from django.views import generic
from .models import Bank   

class ListBank(generic.View):
    template_name = "core/list.html"
    context = {}

    def get(self, request):
        self.context={
            "banks": Bank.objects.all()
        }
        return render(request, self.template_name, self.context)
    
class DetailBank(generic.DetailView):
    template_name= "core/detail.html"
    model = Bank
    context_object_name = "bank"