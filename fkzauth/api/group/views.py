from rest_framework import generics

from fkzauth.groups.models import Group
from fkzauth.groups.serializers import GroupSerializer

class GroupDetails(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

