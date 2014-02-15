from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password

from fkzauth.schools.models import School, Promotion
from fkzauth.students.models import Student

class StudentBackend(object):
    def authenticate(self, forlife, school_id, password):
        """ Authenticates a student using its email and school """
    
        try:
            student = Student.objects.select_related('promotion__formation__school').get(schoolauth__forlife=forlife,promotions__formation__school__pk=school_id)
            # select_related is used for performance reasons
            
            if student.check_password(password):
                return student
            else:
                return None              
        except Student.DoesNotExist:
            # Run the default password hasher once to prevent timing-attacks
            Student.set_password(password)   
            return None  
        
    def get_user(self, user_id):
        
        try:
            return Student.StudentManager.get(pk=user_id)
        except Student.DoesNotExist:
            return None
        
    
