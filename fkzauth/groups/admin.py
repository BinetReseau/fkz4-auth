from django.contrib import admin
from fkzauth.groups.models import Group, GroupMember, GroupRole

admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupRole)

