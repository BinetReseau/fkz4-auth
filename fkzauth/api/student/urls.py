from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from fkzauth.api.student import views

urlpatterns = patterns('',
    url(r'^(?P<pk>[0-9]+)/$', views.StudentDetails.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

