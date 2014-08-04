from rest_framework import generics

from fkzauth.students.models import Student
from fkzauth.students.serializers import StudentSerializer
from fkzauth.api.permissions import IsWebPermission
class StudentDetails(generics.RetrieveAPIView):
    permission_classes=IsWebPermission,
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

