from django import forms
from .models import *

 
class Companyform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("first_name","last_name","birth_date","email","phone_number","narkhi_kitob","suporidansh")
     
     
     
class Bookform(forms.ModelForm):
    class Meta:
        model = Books
        fields = ("books_name","prod_year","zhanr","aftor")   