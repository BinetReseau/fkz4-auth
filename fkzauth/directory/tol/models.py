from fkzauth.students.models import Student
from django.db.models import *
from django.utils.translation import ugettext_lazy as _

class TolEntry(Model):
    image = ImageField(upload_to='tol/',verbose_name=_("Picture"))
    student = ForeignKey(Student,verbose_name=_("Student"))
    class Meta:
        verbose_name=_("Tol Picture")
    def __str__(self):
        return self.image.__str__()
    
class CurrentTolEntry(Model):
    image = ImageField(upload_to='tol/',verbose_name=_("Picture"))
    student=OneToOneField(to=Student,verbose_name=_("Student"))
    class Meta:
        verbose_name=_("Current Tol Picture")

class ToBeValidatedTolEntry(Model):
    image=ImageField(upload_to='tol/',verbose_name=_("Picture"))
    student=ForeignKey(Student,verbose_name=_("Student"))
    class Meta:
        verbose_name=_("To be validated Tol Picture")
    def validate(self):
        current = CurrentTolEntry.objects.filter(student=self.student)
        if current.count()!=0:
            current=current.get()
            newhistory= TolEntry(image=current.image,student=current.student)
            newhistory.save()
            current.delete()
            new = CurrentTolEntry(student=self.student,image=self.image)
            new.save()
            self.delete()
        else:
            new = CurrentTolEntry(student=self.student,image=self.image)
            new.save()
            self.delete()
    def __str__(self):
        return self.image.__str__()