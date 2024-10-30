from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("Rohbar",log_out,name="rohbar"),
    path("Biblioteka",log_out1),
    path("Rohbar_information",infor,name="rohbars"),
    path("Biblioteka_information",infor1,name="biblioteka"),
    path("get_by_student/<int:pk>",get_by_student,name="get_by_id"),
    path("update_company/<int:pk>",update_company,name="update_company"),
    path("add_company",add_company,name="add"),
    path("delete_company/<int:pk>",delete_company,name="delete_company"),
    path("get_by_book/<int:pk>",get_by_book,name="get_by_book"),
    path("update_book/<int:pk>",update_book,name="update_book"),
    path("add_book",add_book,name="add_book"),
    path("delete_book/<int:pk>",delete_book,name="delete_book")
]