from django.contrib import admin
from fkzauth.students.models import Student, SchoolAuth
from fkzauth.groups.models import GroupMember, Group

class GroupMemberInline(admin.TabularInline):
    model = GroupMember
    extra = 1 

class StudentAdmin(admin.ModelAdmin):
    inlines = (GroupMemberInline,)


admin.site.register(Student, StudentAdmin)
admin.site.register(SchoolAuth)
