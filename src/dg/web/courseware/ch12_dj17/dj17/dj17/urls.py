from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'dj17.views.index'),
    url(r'^login/', include('login.urls')),
    url(r'^resume/', include('resume.urls')),
    url(r'^job/', include('job.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
