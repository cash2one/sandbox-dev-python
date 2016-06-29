#encoding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
import controller
from django.template import RequestContext
import dj17.function as fun
import json

from django import forms
class FileForm(forms.Form):
    fileform = forms.FileField()

def company(req):
    if not req.session.get('islogin'):
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    company_info = controller.get_company_info(uid)
    if req.method == "POST":
        data = fun.warp_data(req.POST)
        if not company_info:  ##插入记录
            data['uid'] = uid
            del data['id']
            r = controller.insert_company(data)
        else:  ##更新
            r = controller.update_company(data)
        return HttpResponseRedirect('/job/company')
    else:
        uf = FileForm()
        if not company_info:
            company_info = {}
        return render_to_response('company.html', locals(), context_instance = RequestContext(req))

def upload(req):
    if not req.session.get('islogin'):
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    company_info = controller.get_company_info(uid)
    if not company_info:
        return HttpResponse('please fill base info first!')

    if req.method != "POST":
        return HttpResponse('unsupport method!')

    uf = FileForm(req.POST, req.FILES)
    if uf.is_valid():
        fileform = uf.cleaned_data['fileform']
        print fileform
        f = req.FILES.get('fileform', None)
        if fun.handle_uploaded_file(f):
            company_info.logo = f.name
            company_info.save()
            return HttpResponseRedirect('/job/company')
        else:
            HttpResponse('upload fail!')
    else:
        return HttpResponse('form not avaliable!')


def job(req):
    if not req.session.get('islogin'):
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    if req.method == "GET":
        data = fun.warp_data(req.GET)
        id = data.get('id')
        job_info = controller.get_job_info(id)
        return render_to_response('job.html', locals(), context_instance = RequestContext(req))
    elif req.method == "POST":
        data = fun.warp_data(req.POST)
        data['uid'] = uid
        rt = controller.post_job_info(data)
        if rt:
            msg = '提交职位信息成功'
        else:
            msg = '提交职位信息失败'
        return render_to_response('msg.html', locals())

def list(req):
    if not req.session.get('islogin'):
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    if req.method != "GET":
        return HttpResponse('unsupport method!')
    job_list = controller.get_job_list(uid)
    return render_to_response('job_list.html', locals(), context_instance = RequestContext(req))

def search(req):
    if not req.session.get('islogin'):
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    if req.method != "POST":
        return HttpResponse('unsupport method!')
    keywords = fun.warp_data(req.POST).get('keywords')
    job_list = controller.get_job_search(keywords)
    return render_to_response('job_search.html', locals(), context_instance = RequestContext(req))

def apply(req):
    if not req.session.get('islogin'):
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    if req.method != "POST":
        return HttpResponse('unsupport method!')
    data = fun.warp_data(req.POST)
    data['send_uid'] = uid
    rt = controller.job_apply(data)
    return HttpResponse(json.dumps(rt))

def feedback(req):
    if not req.session.get('islogin'):
        msg = '你当前还没有登录，请先登录！'
        return render_to_response('msg.html', locals())
    uid = req.session['user_info']['id']
    if req.method == "GET":
        data = fun.warp_data(req.GET)
        return render_to_response('job_feedback.html', data, context_instance = RequestContext(req))
    else:
        data = fun.warp_data(req.POST)
        data['is_read'] = 0
        data['create_date'] = fun.now()
        rt = controller.send_feedback(data)
        if rt:
            msg = '职位回执发送成功！'
        else:
            msg = '职位回执发送失败！'
        return render_to_response('msg.html', locals())