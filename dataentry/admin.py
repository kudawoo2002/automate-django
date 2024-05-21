from django.contrib import admin
from dataentry.models import Student, Customer, Employee

# Register your models here.

admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Employee)