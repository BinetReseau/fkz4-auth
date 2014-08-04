from rest_framework import serializers

from fkzauth.students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'firstname', 'lastname', 'email','currenttolentry')
