from django.conf.urls import patterns,include,url
from rest_framework.urlpatterns import format_suffix_patterns
from fkzauth.api.tol import views

urlpatterns = patterns('',
   # url(r'^id=(?P<id>[0-9]+)/$', views.CurrentTolImageView.as_view()),
    #url(r'^id=(?P<id>[0-9]+)/size=(?P<size>.*)/$', views.CurrentTolImageView.as_view()),
   # url(r'^studentid=(?P<studentid>[0-9]+)/$', views.CurrentTolImageView.as_view()),
    url(r'^((studentid=(?P<studentid>[0-9]+)/)|(id=(?P<id>[0-9]+)/)|(size=(?P<size>[^/]*)/))*$', views.CurrentTolImageView.as_view()),
    url(r'^validate/id=(?P<pk>[0-9]+)/$', views.ValidateTolEntryView.as_view()),
)