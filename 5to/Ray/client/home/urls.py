from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('bank/list/',views.ListBankApiView.as_view(),name='list_banks'),
    path('bank/detail/<int:pk>/', views.DetailBankApiView.as_view(), name='detail_bank'),
    path('bank/update/<int:pk>/', views.UpdateBankApiView.as_view(), name='update_bank'),
    path('bank/delete/<int:pk>/', views.DeleteBankApiView.as_view(), name='delete_bank'),
    path('bank/create/', views.CreateBankApiView.as_view(), name='create_bank'),
    path('payment/list/',views.ListPaymentApiView.as_view(),name='list_payments'),
    path('payment/detail/<int:pk>/', views.DetailPaymentApiView.as_view(), name='detail_payment'),
    path('payment/create/', views.CreatePaymentApiView.as_view(), name='create_payment'),
]