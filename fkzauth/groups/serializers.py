from rest_framework import serializers

from fkzauth.groups.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'hruid', 'description', 'image', 'email_prefix', 'wikix_page', 'web_page', 'group_type')
