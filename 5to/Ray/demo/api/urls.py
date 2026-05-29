from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
    #Users EndPoints
    path('v1/users/list', views.UserListApiVIew.as_view(), name="user"),
    #Banks EndPoints
    path('v1/banks/list', views.ListBankApiView.as_view(), name="bank_list"),
    path('v1/banks/detail/<int:pk>', views.DetailBankApiView.as_view(), name="detail_bank"),
    path('v1/banks/create/', views.CreateBankApiView.as_view(), name="create_bank"),
]