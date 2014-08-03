from django.contrib import admin
from fkzauth.students.models import Student, SchoolAuth
from fkzauth.groups.models import GroupMember, Group
from fkzauth.directory.models import NationalityEntry,PhoneNumberEntry
from fkzauth.directory.tol.models import CurrentTolEntry
class GroupMemberInline(admin.TabularInline):
    model = GroupMember
    extra = 1 

class NationalityEntryInline(admin.TabularInline):
    model=NationalityEntry
    extra=1
    
class PhoneNumberEntryInline(admin.TabularInline):
    model=PhoneNumberEntry
    extra=1

class CurrentTolEntryInline(admin.TabularInline):
    model=CurrentTolEntry
    extra=1
    
class StudentAdmin(admin.ModelAdmin):
    inlines = (GroupMemberInline,NationalityEntryInline,PhoneNumberEntryInline,CurrentTolEntryInline)


admin.site.register(Student, StudentAdmin)
admin.site.register(SchoolAuth)
