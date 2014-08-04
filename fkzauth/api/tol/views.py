from rest_framework import generics
from fkzauth.api.permissions import IsWebPermission
from fkzauth.directory.tol.models import ToBeValidatedTolEntry
from rest_framework.response import Response
from django.http.response import HttpResponse, Http404, HttpResponseNotFound
from rest_framework.status import HTTP_404_NOT_FOUND
class ValidateTolEntryView(generics.GenericAPIView):
    permission_classes=IsWebPermission,
    def get(self,*args,**kwargs):
        entry = ToBeValidatedTolEntry.objects.filter(id=kwargs[self.lookup_field])
        if entry.count()==0:
            return HttpResponseNotFound()
        entry=entry.get()
        entry.validate()
        return HttpResponse("OK !")
    