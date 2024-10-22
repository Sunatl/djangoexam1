from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    
    def __str__(self):
        return self.first_name + " " + self.last_name



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Rohbar(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
    
class Biliotekahi(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    
    def __str__(self):
        return self.first_name + " " + self.last_name



class Books(models.Model):
    books_name = models.CharField(max_length=50)
    prod_year = models.DateField()
    zhanr = models.CharField(max_length=60)
    aftor = models.CharField(max_length=60)
    
    def __str__(self):
        return self.first_name + " " + self.last_name