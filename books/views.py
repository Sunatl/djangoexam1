
from django.http import HttpResponse
from django.template import loader


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
    template = loader.get_template("index2.html")
    return HttpResponse(template.render())

def infor1(request):
    template = loader.get_template("index21.html")
    return HttpResponse(template.render())
    