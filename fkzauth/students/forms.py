from django import forms
from django.utils.translation import ugettext_lazy as _
from fkzauth.schools.models import School

class EmailLoginForm(forms.Form):
    email = forms.EmailField(label=_("Email address"))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput())
    next = forms.CharField(widget=forms.HiddenInput())
    
class ForlifeLoginForm(forms.Form):
    forlife = forms.CharField(label=_("Your school's identifier"))
    
    schools = School.objects.all()
    school_list = []
    for s in schools:
        school_list.append((s.pk, s.suffix)) 
    
    school_id = forms.ChoiceField(choices=school_list)
    
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput())
    next = forms.CharField(widget=forms.HiddenInput())
