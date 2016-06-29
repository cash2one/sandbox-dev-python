from django.conf.urls import patterns, include, url

urlpatterns = patterns('resume.views',
    url(r'^default', 'default'),
    url(r'^post', 'post'),
    url(r'^work', 'work'),
    url(r'^study', 'study'),
    url(r'^search', 'search'),
    url(r'^upload', 'upload'),
)
