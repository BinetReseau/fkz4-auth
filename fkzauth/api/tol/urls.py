from django.conf.urls import patterns,include,url
from rest_framework.urlpatterns import format_suffix_patterns
from fkzauth.api.tol import views

urlpatterns = patterns('',
    url(r'^validate/id=(?P<pk>[0-9]+)/$', views.ValidateTolEntryView.as_view()),
)