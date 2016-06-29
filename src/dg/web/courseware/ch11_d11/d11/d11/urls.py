from django.conf.urls import patterns, include, url
from django.contrib import admin
from d11.views import hello,hours_ahead,templates,temp2,temp3,test
import books
from django.contrib.auth.views import login, logout
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'd11.views.home', name='home'),
    url(r'^hello$', hello),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^templates/$', templates),
    url(r'^temp2/$', temp2),
    url(r'^temp3/$', temp3),
    url(r'^test/$', test),
    url(r'^child/$', 'd11.views.child'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include(books.urls)),

    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
)
