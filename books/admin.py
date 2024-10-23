from django.contrib import admin

from .models import Student,Adress,City,Region,Books


admin.site.register(City)
admin.site.register(Books)
admin.site.register(Adress)
admin.site.register(Student)
admin.site.register(Region)