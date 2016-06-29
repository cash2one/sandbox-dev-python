#encoding: utf-8
__author__ = 'xwchen2'

from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from login.models import User,Resume,Company,Job

def index(req):
    users = User.objects.all()
    resumes = Resume.objects.all()
    companys = Company.objects.all()
    jobs = Job.objects.all()
    # print users
    return render_to_response('index.html', locals(), context_instance = RequestContext(req))

