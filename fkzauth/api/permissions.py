
from rest_framework import permissions
from fkzauth.groups.models import GroupMember,Group
WEB_GROUP_HRUID='web'

class IsWebPermission (permissions.BasePermission):
    def has_permission(self,request,view):
        user=request.user
        if user == None :
            return False
        webgroup=Group.objects.filter(hruid=WEB_GROUP_HRUID)
        if(webgroup.count()==0):
            return False
        webgroup=webgroup.get()
        membership=GroupMember.objects.filter(student=user,group=webgroup).count()==1
        return membership

        