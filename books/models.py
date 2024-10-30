from django.db import models




class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(max_length=254) 
    phone_number = models.CharField(max_length=13) 
    narkhi_kitob = models.CharField(max_length=(50),default=150) 
    suporidansh = models.CharField(max_length=(50),default=False)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    

        


    
    


class Books(models.Model):
    books_name = models.CharField(max_length=50)
    prod_year = models.DateField()
    zhanr = models.CharField(max_length=60)
    aftor = models.CharField(max_length=60)
    
    def __str__(self):
        return self.books_name