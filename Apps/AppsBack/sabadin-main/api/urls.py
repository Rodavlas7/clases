from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('list/banks/', views.ListBank.as_view(), name="list"),
    path('create/banks/', views.CreateBank.as_view(), name="create"),
    path('detail/banks/<int:pk>/', views.DetailBan.as_view(), name="detail"),
    path('update/banks/<int:pk>/', views.Update.as_view(), name="update"),
    path('delete/banks/<int:pk>/', views.Delete.as_view(), name="delete")
]
