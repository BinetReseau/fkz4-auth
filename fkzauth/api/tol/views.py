from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from fkzauth.api.permissions import IsWebPermission
from fkzauth.directory.tol.models import *
from django.http.response import HttpResponse, Http404, HttpResponseNotFound
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from django.core.files.base import File
from wsgiref.util import FileWrapper

class ValidateTolEntryView(generics.GenericAPIView):
    permission_classes=IsWebPermission,
    def get(self,*args,**kwargs):
        entry = ToBeValidatedTolEntry.objects.filter(id=kwargs[self.lookup_field])
        if entry.count()==0:
            return HttpResponseNotFound()
        entry=entry.get()
        entry.validate()
        return HttpResponse("OK !")

class CurrentTolImageView(generics.GenericAPIView):
    permission_classes=IsAuthenticated,
    def get(self,*args,**kwargs):
        if('id' in kwargs):
            self.id=kwargs['id']
            currentTol=CurrentTolEntry.objects.filter(id=self.id)
        elif 'studentid' in kwargs:
            self.studentid=kwargs['studentid']
            currentTol=CurrentTolEntry.objects.filter(student__id=self.studentid)
        if(currentTol.count()==0):
            return HttpResponseNotFound()
        currentTol=currentTol.get()
        path=currentTol.image.path
        f=open(path,'rb')
        response = HttpResponse(FileWrapper(f),content_type='image/png')
        return response
            
            
            
