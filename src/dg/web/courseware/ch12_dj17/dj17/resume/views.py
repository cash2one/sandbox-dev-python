#encoding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
import controller
from django.template import RequestContext
import dj17.function as fun

from django import forms
class FileForm(forms.Form):
    fileform = forms.FileField()

def default(req):
    if not req.session['islogin']:
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    resume_info = controller.get_resume_info(uid)
    if resume_info:
        resume_id = resume_info.id
        work_experience = controller.get_work_experience(resume_id)
        # print work_experience[0].start_date
        study_experience = controller.get_study_experience(resume_id)
    else:
        resume_info = {}
    uf = FileForm()
    return render_to_response('resume.html', locals(), context_instance = RequestContext(req))

def post(req):
    if not req.session['islogin']:
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    if req.method != "POST":
        return HttpResponse('unsupport method!')
    data = fun.warp_data(req.POST)
    uid = req.session['user_info']['id']
    data['uid'] = uid
    rt = controller.resume_post(data)
    if rt:
        return HttpResponseRedirect('/resume/default')
    else:
        msg = '提交简历失败,请联系管理员！'
        return render_to_response('msg.html', locals())

def work(req):
    if not req.session['islogin']:
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    if req.method != "POST":
        return HttpResponse('unsupport method!')
    data = fun.warp_data(req.POST)
    rt = controller.resume_work(data)
    # print rt
    if rt:
        return HttpResponseRedirect('/resume/default')
    else:
        msg = '提交工作经验失败,请联系管理员！'
        return render_to_response('msg.html', locals())

def study(req):
    if not req.session['islogin']:
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    if req.method != "POST":
        return HttpResponse('unsupport method!')
    data = fun.warp_data(req.POST)
    rt = controller.resume_study(data)
    if rt:
        return HttpResponseRedirect('/resume/default')
    else:
        msg = '提交工作经验失败,请联系管理员！'
        return render_to_response('msg.html', locals())

def upload(req):
    if not req.session['islogin']:
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    resume_info = controller.get_resume_info(uid)
    if not resume_info:
        return HttpResponse('please fill base info first!')

    if req.method != "POST":
        return HttpResponse('unsupport method!')

    uf = FileForm(req.POST, req.FILES)
    if uf.is_valid():
        fileform = uf.cleaned_data['fileform']
        f = req.FILES.get('fileform', None)
        if fun.handle_uploaded_file(f):
            resume_info.attach_file = f.name
            resume_info.save()
            return HttpResponseRedirect('/resume/default')
        else:
            return HttpResponse('upload fail!')
    else:
        return HttpResponse('form not avaliable!')

def search(req):
    data = fun.warp_data(req.POST)
    keywords = data.get('keywords')
    resume_list = controller.resume_search(keywords)
    return render_to_response('resume_search.html', locals(), context_instance = RequestContext(req))
