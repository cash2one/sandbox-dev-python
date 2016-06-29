#!/usr/bin/env python
#coding=utf-8
from django.shortcuts import render_to_response,RequestContext
from books.models import Publisher

def index(req):
    msg = u'book 首页'
    return render_to_response('books/index.html', locals())

def author(req):
    if req.method == 'POST':
        data = req.POST
        print data
    return render_to_response('books/author.html', locals(), context_instance=RequestContext(req))

def login(req):
    return render_to_response('books/login.html', locals())

from django.http import Http404, HttpResponse, HttpResponseRedirect
def setCookie(req):
    HttpResponse.set_cookie("favorite_color","values", expires=-1)

def isLogin(req):
    if req.user.is_authenticated():
        pass
        # Do something for authenticated users.
    else:
        pass
        # Do something for anonymous users.


    # myuser = req.user
    # # Set a user's groups:
    # myuser.groups = group_list
    # # Add a user to some groups:
    # myuser.groups.add(group1, group2,...)
    # # Remove a user from some groups:
    # myuser.groups.remove(group1, group2,...)
    # # Remove a user from all groups:
    # myuser.groups.clear()
    # # Permissions work the same way
    # myuser.permissions = permission_list
    # myuser.permissions.add(permission1, permission2, ...)
    # myuser.permissions.remove(permission1, permission2, ...)
    # myuser.permissions.clear()

from django.contrib import auth
def login(req):
    user = auth.authenticate(username='john', password='secret')
    if user is not None:
        print "Correct!"
    else:
        print "Invalid password."

def logout(req):
    auth.logout(req)
    return HttpResponseRedirect("/account/loggedout/")

from django.contrib.auth.views import login, logout

def dbtest(req):
    ##插入记录
    p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
            city='Berkeley', state_province='CA', country='U.S.A.',
            website='http://www.apress.com/')
    p1.save() ##插入记录
    print p1.id
    p1.name = 'Apress Publishing'
    p1.save() ##更新记录

    p2 = Publisher.objects.create(name="O'Reilly",
            address='10 Fawcett St.', city='Cambridge',
            state_province='MA', country='U.S.A.',
            website='http://www.oreilly.com/')
    ##查询记录与过滤
    publisher_list = Publisher.objects.all()
    print publisher_list
    publisher_list = Publisher.objects.filter(name='Apress')
    print publisher_list
    publisher_list = Publisher.objects.filter(country="U.S.A.", state_province="CA")
    Publisher.objects.filter(name__contains="press")
    ##icontains(大小写无关的LIKE),startswith和endswith, 还有range(SQLBETWEEN查询)
    publisher = Publisher.objects.get(name="Apress")  ##如果结果是多个对象，会导致抛出异常,没有返回结果也会抛出异常
    Publisher.objects.order_by("name")  ##排序
    Publisher.objects.filter(country="U.S.A.").order_by("-name")
    Publisher.objects.order_by('name')[0]  ##限制数据，等同于limit
    ##更新
    p = Publisher.objects.get(name='Apress')
    p.name = 'Apress Publishing'
    p.save()
    Publisher.objects.filter(id=52).update(name='Apress Publishing')
    Publisher.objects.all().update(country='USA')
    ##删除
    p = Publisher.objects.get(name="O'Reilly")
    p.delete()
    Publisher.objects.filter(country='USA').delete()
    Publisher.objects.all().delete()


