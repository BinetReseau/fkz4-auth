from django.contrib import admin
from fkzauth.directory.rooms.models import Residence,Room,StudentInRoom
admin.site.register(Residence)
admin.site.register(Room)
admin.site.register(StudentInRoom)