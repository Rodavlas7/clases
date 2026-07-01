from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
    #Users EndPoints
    path('v1/users/list', views.UserListApiVIew.as_view(), name="user"),
    #Banks EndPoints
    path('v1/banks/list', views.ListBankApiView.as_view(), name="bank_list"),
    path('v1/banks/detail/<int:pk>', views.DetailBankApiView.as_view(), name="detail_bank"),
    path('v1/banks/update/<int:pk>', views.UpdateBankApiView.as_view(), name="update_bank"),
    path('v1/banks/create/', views.CreateBankApiView.as_view(), name="create_bank"),
    path('v1/banks/delete/<int:pk>', views.DeleteBankApiView.as_view(), name="delete_bank"),
    path('v2/account/list/', views.ListAccountApiView.as_view(), name="list_account"),
    path('v2/account/detail/<int:pk>', views.DetailAccountApiView.as_view(), name="detail_account"),
    path('v2/payment/list/', views.ListPaymentApiView.as_view(), name="list_payment"),
    path('v2/payment/detail/<int:pk>', views.DetailPaymentApiView.as_view(), name="detail_payment"),
    path('v2/payment/create/', views.CreatePaymentApiView.as_view(), name="create_payment"),
]