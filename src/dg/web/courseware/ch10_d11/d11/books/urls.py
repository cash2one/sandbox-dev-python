from django.conf.urls import patterns, url

urls = patterns('books.views',
    url(r'^$', 'index'),
    url(r'^author/$', 'author'),
    url(r'^login/$', 'login'),
    )