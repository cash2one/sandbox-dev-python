from django.http import Http404, HttpResponse

def home(request):
    print dir(request)
    print type(request)
    return HttpResponse('Welcome to My Home Page')

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')

import datetime
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

from django.template import Template, Context
def templates(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

from django.template.loader import get_template
def temp2(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

from django.shortcuts import render_to_response
def temp3(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

def test(request):
    current_date = datetime.datetime.now()
    return render_to_response('test.html', locals())

def child(request):
    current_date = datetime.datetime.now()
    return render_to_response('child.html', locals())

