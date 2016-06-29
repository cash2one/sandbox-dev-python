#!/usr/bin/env python
#coding=utf-8
from django.shortcuts import render_to_response,RequestContext
from books.models import Publisher,Book,Author
from django.http import Http404, HttpResponse, HttpResponseRedirect

def index(req):
    msg = u'book 首页'

    req.session['user'] = 'macy'
    print req.session['user']

    print req.META
    print req.META.get('PATH_INFO')

    print req.COOKIES
    response = render_to_response('books/index.html', locals())
    response.set_cookie("favorite_color","values")

    response['django'] = '1.7.7'
    return response

from django import forms
class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

def file_upload(req):
    if req.method == "POST":
        uf = UserForm(req.POST, req.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            print headImg
            f = req.FILES.get('headImg', None)
            handle_uploaded_file(f)
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('books/fileupload.html',{'uf':uf})

def handle_uploaded_file(f):
    print dir(f)
    destination = open('upload/%s' % f.name,'wb')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

from django.contrib import auth
def login(req):
    if req.method == 'GET':
        return render_to_response('books/login.html', locals(), context_instance=RequestContext(req))
    data = req.POST
    username = data.get('username')
    password = data.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(req, user)
        print "Correct!"
        msg = 'login pass'
        return render_to_response('msg.html', locals())
    else:
        print "Invalid password."
        msg = 'login fail'
        return render_to_response('msg.html', locals())

def logout(req):
    auth.logout(req)
    msg = 'logout pass'
    return render_to_response('msg.html', locals())

def isLogin(req):
    if req.user.is_authenticated():
        pass
        # Do something for authenticated users.
    else:
        pass
        # Do something for anonymous users.

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

def user_permissions(req):
    # myuser = req.user
    # # Set a user's groups:
    # myuser.groups = group_list
    # # Add a user to some groups:
    # myuser.groups.add(group1, group2)
    # # Remove a user from some groups:
    # myuser.groups.remove(group1, group2)
    # # Remove a user from all groups:
    # myuser.groups.clear()
    # # Permissions work the same way
    # myuser.permissions = permission_list
    # myuser.permissions.add(permission1, permission2)
    # myuser.permissions.remove(permission1, permission2)
    # myuser.permissions.clear()
    pass

def bookauthor(req):
    if req.method == 'POST':
        data = req.POST
        print data
    return render_to_response('books/bookauthor.html', locals(), context_instance=RequestContext(req))

def one_v_more(req):
    p = Publisher.objects.get(name='china book')
    all = p.book_set.all()
    print all
    f = p.book_set.filter(title__icontains='django')
    print f
    return HttpResponse('%s<br>%s'% (len(all), len(f)))

def many_to_many(req):
    b = Book.objects.get(id=2)
    print b.authors.all()
    print b.authors.filter(first_name='xiaowu')

    a = Author.objects.get(first_name='xiaowu', last_name='chen')
    print a.book_set.all()

    return HttpResponse('查询成功')

def exec_sql(req):
    from django.db import connection
    cursor = connection.cursor()
    sql = "select * from books_author"
    cursor.execute(sql)
    row = cursor.fetchone()
    print row
    return HttpResponse('%s'% str(row))