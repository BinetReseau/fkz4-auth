from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from fkzauth.api import views

urlpatterns = patterns('',
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentDetails.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

