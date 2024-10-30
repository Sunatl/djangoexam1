
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Student,Books
from .form import *

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




def get_by_student(request,pk):
    tasks  = Student.objects.filter(id=pk).first()
    if tasks:
        return render(request,"main.html",context={"students":tasks})
    else:
        return HttpResponse("Tasks object not found")
    
    
    
def update_company(request,pk):
    tasks  = Student.objects.filter(id=pk).first()   
    if tasks:
        if request.method == "POST":
            form  = Companyform(request.POST,request.FILES, instance=tasks)
            if form .is_valid():
                form.save()
                return redirect("rohbars")
        else:
            form = Companyform(instance=tasks)
            
        return render(request,"index1.html", context={"form":form})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")


def delete_company(request,pk):
    tasks =  Student.objects.filter(id = pk).first()
    if tasks:
        if request.method == "POST":
            tasks.delete()
            return redirect("rohbars")
        else:
            return render(request,"main1.html",context={"tasks":tasks})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")


    
def add_company(request):
    if request.method == "POST":
        form  = Companyform(request.POST,request.FILES )
        if form .is_valid():
            form.save()
            return redirect("rohbars")
    else:
        form = Companyform()
    return render(request,"add.html", context={"form":form})





def get_by_book(request,pk):
    tasks  = Books.objects.filter(id=pk).first()
    if tasks:
        return render(request,"get_book.html",context={"students":tasks})
    else:
        return HttpResponse("Tasks object not found")
    
    
    
def update_book(request,pk):
    tasks  = Books.objects.filter(id=pk).first()   
    if tasks:
        if request.method == "POST":
            form  = Bookform(request.POST,request.FILES, instance=tasks)
            if form .is_valid():
                form.save()
                return redirect("biblioteka")
        else:
            form = Bookform(instance=tasks)
            
        return render(request,"update.html", context={"form":form})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")


def delete_book(request,pk):
    tasks =  Books.objects.filter(id = pk).first()
    if tasks:
        if request.method == "POST":
            tasks.delete()
            return redirect("biblioteka")
        else:
            return render(request,"delete.html",context={"tasks":tasks})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")


    
def add_book(request):
    if request.method == "POST":
        form  = Bookform(request.POST,request.FILES )
        if form .is_valid():
            form.save()
            return redirect("biblioteka")
    else:
        form = Bookform()
    return render(request,"add_book.html", context={"form":form})