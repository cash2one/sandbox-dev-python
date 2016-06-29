from django.conf.urls import patterns, url

urls = patterns('books.views',
    url(r'^$', 'index'),
    url(r'^bookauthor/$', 'bookauthor'),
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
    url(r'^fileupload/$', 'file_upload'),
    url(r'^one_v_more/$', 'one_v_more'),
    url(r'^many_to_many/$', 'many_to_many'),
    url(r'^execsql/$', 'exec_sql'),
    )