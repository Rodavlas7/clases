from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path('list/banks/', views.ListBank.as_view(), name="list"),
    path('detail/banks/<int:pk>/', views.DetailBank.as_view(), name="detail")
]
