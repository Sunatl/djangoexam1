from django.urls import path
from .views import home,log_in,log_out,log_out1,infor,infor1

urlpatterns = [
    path("Register", log_in),
    path("Books_online",home),
    path("Rohbar",log_out),
    path("Biblioteka",log_out1),
    path("Rohbar_information",infor),
    path("Biblioteka_information",infor1)
]