from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models

from fkzauth.schools.models import School, Promotion


class StudentManager(BaseUserManager):
    """
    Class managing students
    """
    def create_user(self, firstname, lastname, email, promotions, forlife_schools, password):
        """
        Creates and saves the student identification informations
        """
        student = self.model(
            firstname=firstname,
            lastname=lastname,
            email=self.normalize_email(email),
            promotions=promotions,
            forlife_schools=forlife_schools
            )
        
        student.set_password(password)
        student.save(using=self._db)
        
        return student
        
    def create_super_user(self, firstname, lastname, email, promotions, forlife_schools, password):
        """
        Creates and saves the infrormations about a superuser (= admin)
        """
        student = self.model(
            firstname=firstname,
            lastname=lastname,
            email=self.normalize_email(email),
            promotions=promotions,
            forlife_schools=forlife_schools
            )
            
        student.set_password(password)
        student.is_staff = True
        student.save(using=self._db)
        
        return student

class Student(AbstractBaseUser):
    """
    Class representing a Student, used for authentication.
    """
    firstname = models.CharField(max_length=50, verbose_name=_("firstname"))
    lastname = models.CharField(max_length=50, verbose_name=_("lastname"))
    email = models.EmailField(max_length=254, verbose_name=_("email"), unique=True)
    
    #Fields needed to be compatible with the Admin interface
    is_staff = models.BooleanField(default=False, verbose_name=_("staff member"))
    is_active = models.BooleanField(default=True, verbose_name=_("active account"))

    USERNAME_FIELD = 'email'

# authentication details :

    promotions = models.ManyToManyField(Promotion, related_name='students', verbose_name="promotions")

    forlife_schools = models.ManyToManyField(School, related_name='student_auths', 
                    through='SchoolAuth', verbose_name=_("institutional emails for authentication"))

    objects = StudentManager()

    def get_full_name(self):
        # The user is identified by their email address
        return "%s %s <%s>" % (self.firstname, self.lastname, self.email)

    def get_short_name(self):
        # The user is identified by their email address
        return "%s %s" % (self.firstname, self.lastname, self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    
    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
    

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
        return "%s@%s" % (self.forlife, self.school.suffix)

