from django.conf.urls import patterns, include, url

urlpatterns = patterns('job.views',
    url(r'^company', 'company'),
    url(r'^upload', 'upload'),
    url(r'^job', 'job'),
    url(r'^list', 'list'),
    url(r'^search', 'search'),
    url(r'^apply', 'apply'),
    url(r'^feedback', 'feedback'),
)
