from django.contrib import admin
from fkzauth.directory.models import *
# Register your models here.
admin.site.register(PhoneNumberEntry)
admin.site.register(Nationality)
admin.site.register(NationalityEntry)