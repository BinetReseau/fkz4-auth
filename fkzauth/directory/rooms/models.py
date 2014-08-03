from django.db import models
from django.db.models import *
from django.core.validators import * 
from django.utils.translation import ugettext_lazy as _

class Residence(models.Model):
    picture=ImageField(upload_to="residence_pictures/",blank=True,null=True,verbose_name=_("Picture of the Residence"))
    name=TextField(verbose_name="Name of the residence")
    def __str__(self):
        return self.name
    
class Room(Model):
    residence=ForeignKey(Residence,verbose_name=_("Residence of the room"))
    identifier=CharField(max_length=255,verbose_name=_("identifier of the room"))
    students=ManyToManyField(to="students.Student",through="StudentInRoom")
    def __str__(self):
        return "%s %s"%(_("Room"),self.identifier)

class StudentInRoom(Model):
    year=IntegerField(verbose_name=_("Year of entering the room"))
    student=ForeignKey(to="students.Student",verbose_name=_("Student"))
    room=ForeignKey(to="Room",verbose_name=_("room"))
    class Meta:
        unique_together=("year","room")
    def __str__(self):
        return "Year %s : %s in %s"%(self.year,self.student,self.room)
    
    

