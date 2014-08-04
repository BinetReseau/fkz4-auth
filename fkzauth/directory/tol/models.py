from fkzauth.students.models import Student
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from PIL import Image
TOL_IMAGE_BIG_SIZE=480,640
TOL_IMAGE_MEDIUM_SIZE=240,320
TOL_IMAGE_SMALL_SIZE=128,128

class TolEntry(Model):
    image = ImageField(upload_to='tol/',verbose_name=_("Picture"))
    class Meta:
        abstract = True
    
    def save(self):
        super(TolEntry,self).save()
        path=self.image.path
        image=Image.open(path)
        image.thumbnail(TOL_IMAGE_BIG_SIZE,Image.ANTIALIAS)
        image.save(path+".big","JPEG")
        image=Image.open(path)
        image.thumbnail(TOL_IMAGE_MEDIUM_SIZE,Image.ANTIALIAS)
        image.save(path+".medium","JPEG")
        image=Image.open(path)
        image.thumbnail(TOL_IMAGE_SMALL_SIZE,Image.ANTIALIAS)
        image.save(path+".small","JPEG")
        
        
class HistoryTolEntry(TolEntry):
    student = ForeignKey(Student,verbose_name=_("Student"))
    class Meta:
        verbose_name=_("Former Tol Picture")
    def __str__(self):
        return self.image.__str__()
    
class CurrentTolEntry(TolEntry):
    student=OneToOneField(to=Student,verbose_name=_("Student"))
    class Meta:
        verbose_name=_("Current Tol Picture")

class ToBeValidatedTolEntry(TolEntry):
    student=ForeignKey(Student,verbose_name=_("Student"))
    class Meta:
        verbose_name=_("To be validated Tol Picture")
    def validate(self):
        current = CurrentTolEntry.objects.filter(student=self.student)
        if current.count()!=0:
            current=current.get()
            newhistory= HistoryTolEntry(image=current.image,student=current.student)
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

