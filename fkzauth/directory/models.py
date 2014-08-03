from django.db import models
from django.core.validators import * 
from django.utils.translation import ugettext_lazy as _

class DirectoryInformation(models.Model):
    POSSIBLE_CONFIDENTIALITY_LEVELS=(("all",_("Everyone can see")),("school",_("People in my school")),("std",_("People who study with me")))
    confidentialityLevel=models.CharField(max_length=4,choices=POSSIBLE_CONFIDENTIALITY_LEVELS,default="all",verbose_name=_("Who can see this"))
    student=models.ForeignKey("students.Student",verbose_name=_("Student"))
    class Meta:
        abstract=True

class Nationality(models.Model):
    flag=models.ImageField(upload_to="flags/images")
    name=models.CharField(max_length=50,verbose_name=_("display name of the nationality"))
    class Meta:
        verbose_name=_("Nationality")
    def __str__(self):
        return "%s"%self.name

class NationalityEntry(models.Model):
    nationality=models.ForeignKey("Nationality",verbose_name=_("Nationality"),)
    student=models.ForeignKey("students.Student",verbose_name=_("Student"),)

class PhoneNumberEntry(DirectoryInformation):
    phoneNumber=models.IntegerField(verbose_name=_("Phone number"),)
    