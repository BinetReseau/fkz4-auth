from django.contrib import admin
from fkzauth.directory.tol.models import *
admin.site.register(HistoryTolEntry)
admin.site.register(CurrentTolEntry)
admin.site.register(ToBeValidatedTolEntry)
