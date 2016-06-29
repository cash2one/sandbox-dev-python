#encoding: utf-8
__author__ = 'xwchen2'

from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from login.models import User,Resume,Company,Job, JobApply, JobFeedback

def index(req):
    users = User.objects.all()
    resumes = Resume.objects.all()
    companys = Company.objects.all()
    jobs = Job.objects.all()
    # print users
    return render_to_response('index.html', locals(), context_instance = RequestContext(req))

def message(req):
    if not req.session.get('islogin'):
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    job_apply = JobApply.objects.filter(uid=uid).order_by('-create_date')
    job_feedback = JobFeedback.objects.filter(uid=uid).order_by('-create_date')
    return render_to_response('message.html', locals(), context_instance = RequestContext(req))