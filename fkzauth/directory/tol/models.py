from fkzauth.students.models import Student
from django.db.models import *
from django.utils.translation import ugettext_lazy as _

class TolEntry(Model):
    image = ImageField(upload_to='tol/',verbose_name=_("Picture"))
    student = ForeignKey(Student,verbose_name=_("Student"))
    class Meta:
        verbose_name=_("Tol Picture")
    def validate(self):
        current = CurrentTolEntry.objects.get(student=self.student)
        current.delete()
        new = CurrentTolEntry(student=self.student,image=self.image)
        new.save()
    def __str__(self):
        return self.image.__name__
    
class CurrentTolEntry(Model):
    image = ImageField(upload_to='tol/',verbose_name=_("Picture"))
    student=OneToOneField(to=Student,verbose_name=_("Student"))
    class Meta:
        verbose_name=_("Current Tol Picture")
    