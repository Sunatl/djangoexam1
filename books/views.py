
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .models import Student,Books
from .form import *

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def log_in(request):
    template = loader.get_template("index1.html")
    return HttpResponse(template.render())

def log_out(request):
    template = loader.get_template("index11.html")
    return HttpResponse(template.render())

def log_out1(request):
    template = loader.get_template("index22.html")
    return HttpResponse(template.render())




class StudentList(ListView):
    model = Student
    template_name = 'index2.html' 



class StudentDetailView(DetailView):
    model = Student
    template_name = 'main.html'
    
    
    
class StudentUpdate(UpdateView):
    model = Student
    template_name = 'index1.html'  
    fields = ['first_name','last_name','birth_date', 'email','phone_number','narkhi_kitob','suporidansh']
    success_url = reverse_lazy('rohbars') 


class StudentDelete(DeleteView):
    model = Student
    template_name = 'main1.html' 
    success_url = reverse_lazy('rohbars')  


    
class StudentCreateView(CreateView):
    model = Student
    template_name = 'add.html'
    fields = ['first_name','last_name','birth_date', 'email','phone_number','narkhi_kitob','suporidansh']
    success_url = reverse_lazy('rohbars') 










# BOOKSTUDENT

class BookListView(ListView):
    model = Books
    template_name = 'index21.html'  

class BookDetailView(DetailView):
    model = Books
    template_name = 'get_book.html'
    
    
    
class BookUpdateView(UpdateView):
    model = Books
    template_name = 'update.html'  
    fields = ['books_name','prod_year','zhanr', 'aftor']
    success_url = reverse_lazy('biblioteka') 

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'delete.html' 
    success_url = reverse_lazy('biblioteka')  


    
class BookCreateView(CreateView):
    model = Books
    template_name = 'add_book.html'
    fields = ['books_name','prod_year','zhanr', 'aftor']
    success_url = reverse_lazy('biblioteka') 