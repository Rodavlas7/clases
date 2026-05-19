from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
    #Users EndPoints
    path('v1/users/list', views.UserListApiVIew.as_view(), name="user_view"),
]