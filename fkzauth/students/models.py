from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.db import models

from fkzauth.schools.models import School, Promotion

class Student(AbstractBaseUser):
    """
    Class representing a Student, used for authentication.
    """
    firstname = models.CharField(max_length=50, verbose_name=_("fristname"))
    lastname = models.CharField(max_length=50, vebose_name=_("lastname"))
    email = models.EmailField(max_length=254, verbose_name=_("email"), unique=True)

    USERNAME_FIELD = 'email'

# authentication details :

    promotions = models.ManyToManyField(Promotion, related_name='students', verbose_name="promotions")

    forlife_schools = models.ManyToManyField(School, related_name='student_auths', 
                    through='SchoolAuth', verbose_name=_("institutional emails for authentication"))

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def __self__(self):
        return "%(self.firstname) %(self.lastname)" % self

class SchoolAuth(models.Model):
    """
    Class holding the student forlife given by its school.
    """
    student = models.ForeignKey(Student, verbose_name=_("student"))
    school = models.ForeignKey(School, verbose_name=_("school"))
    forlife = models.SlugField(max_length=120, verbose_name=_("forlife"))

    class Meta:
        verbose_name = _("school forlife")
        verbose_name_plural = _("school forlifes")
        unique_together = ('school','forlife')

    def __str__(self):
        return "%(self.forlife)@%(self.school.suffix)" % self
