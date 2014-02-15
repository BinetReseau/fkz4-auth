from django.contrib import admin
from fkzauth.students.models import Student, SchoolAuth

admin.site.register(Student)
admin.site.register(SchoolAuth)
