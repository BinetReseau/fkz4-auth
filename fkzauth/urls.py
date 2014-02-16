from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fkzauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #OAuth
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #API
    url(r'^api/', include('fkzauth.api.urls', namespace='api')),
    #Login
    url(r'^login/', include('fkzauth.students.urls', namespace='login')),
)
