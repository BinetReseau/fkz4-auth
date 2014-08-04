from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
	url(r'^student/', include('fkzauth.api.student.urls', namespace='api')),
	url(r'^group/', include('fkzauth.api.group.urls', namespace='api')),
	url(r'^tol/',include('fkzauth.api.tol.urls',namespace='api'))
)

urlpatterns = format_suffix_patterns(urlpatterns)

