from rest_framework import generics

from fkzauth.groups.models import Group, GroupMember
from fkzauth.groups.serializers import GroupSerializer, GroupMemberSerializer

class GroupDetails(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupMembers(generics.RetrieveAPIView):
    queryset = GroupMember.objects.all()
    lookup_field = 'group__id'
    serializer_class = GroupMemberSerializer

