from django.urls import path
from frontend import views

app_name = "home"


urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('list/', views.ListServiciosApiView.as_view(), name="list_servicio"),
    path('<int:pk>/', views.DetailServicioApiView.as_view(), name="detail_servicio"),
    path('create/', views.CreateServicioView.as_view(), name="create_servicio"),
    path('update/<int:pk>/', views.UpdateServicioView.as_view(), name="update_servicio"),
    path('delete/<int:pk>/', views.DeleteServicioView.as_view(), name="delete_servicio"),
]
