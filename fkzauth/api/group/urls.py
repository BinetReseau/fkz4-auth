from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from fkzauth.api.group import views

urlpatterns = patterns('',
	url(r'^id=(?P<pk>[0-9]+)/$', views.GroupDetails.as_view()),
	url(r'^members/id=(?P<group__id>[0-9]+)/$', views.GroupMembers.as_view()),
)

#urlpatterns = format_suffix_patterns(urlpatterns)

