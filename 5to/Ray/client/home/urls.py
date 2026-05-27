from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('list/banks',views.ListBankApiView.as_view(),name='list_banks'),
    path('banks/detail/<int:pk>/', views.DetailBankApiView.as_view(), name='detail_bank'),
]