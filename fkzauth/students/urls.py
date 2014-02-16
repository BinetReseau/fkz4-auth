from django.conf.urls import patterns, include, url
from .views import LoginView

urlpatterns = patterns('',
    url(r'^$', LoginView.as_view()),
    url(r'^(?P<mode>\w+)/$', LoginView.as_view()),

)
