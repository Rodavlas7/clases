from django.urls import path
from servicios import views

urlpatterns = [
    path('', views.ListServicioApiView.as_view(), name="list_servicio"),
    path('<int:pk>/', views.DetailServicioApiView.as_view(), name="detail_servicio"),
    path('create/', views.CreateServicioApiView.as_view(), name="create_servicio"),
    path('update/<int:pk>/', views.UpdateServicioApiView.as_view(), name="update_servicio"),
    path('delete/<int:pk>/', views.DeleteServicioApiView.as_view(), name="delete_servicio"),
]
