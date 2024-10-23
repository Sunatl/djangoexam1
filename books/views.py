
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Student,Books

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

def infor(request):
    students = Student.objects.all()
    return render(request,'index2.html',context={"students": students})

def infor1(request):
    books = Books.objects.all()
    return render(request,'index21.html',context={"books": books})



    