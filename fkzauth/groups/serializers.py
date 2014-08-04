from rest_framework import serializers

from fkzauth.groups.models import Group, GroupMember

class GroupSerializer(serializers.ModelSerializer):
    image = serializers.Field('image.url')
    class Meta:
        model = Group
        fields = ('id', 'name', 'hruid', 'description', 'image', 'email_prefix', 'wikix_page', 'web_page', 'group_type')

class GroupMemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = GroupMember
		fields = ('student', 'group', 'status', 'visible', 'message')
