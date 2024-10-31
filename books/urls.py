from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("Rohbar",log_out,name="rohbar"),
    path("Biblioteka",log_out1),
    path("Rohbar_information",StudentList.as_view(),name="rohbars"),
    path("Biblioteka_information",BookListView.as_view(),name="biblioteka"),
    path("get_by_student/<int:pk>",StudentDetailView.as_view(),name="get_by_id"),
    path("update_company/<int:pk>",StudentUpdate.as_view(),name="update_student"),
    path("add_company",StudentCreateView.as_view(),name="add"),
    path("delete_company/<int:pk>",StudentDelete.as_view(),name="delete_student"),
    path("get_by_book/<int:pk>",BookDetailView.as_view(),name="get_by_book"),
    path("update_book/<int:pk>",BookUpdateView.as_view(),name="update_book"),
    path("add_book",BookCreateView.as_view(),name="add_book"),
    path("delete_book/<int:pk>",BookDeleteView.as_view(),name="delete_book")
]