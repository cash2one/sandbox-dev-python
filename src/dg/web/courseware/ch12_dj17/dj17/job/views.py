#encoding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
import controller
from django.template import RequestContext
import dj17.function as fun

from django import forms
class FileForm(forms.Form):
    fileform = forms.FileField()

def company(req):
    if not req.session['islogin']:
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
    if not req.session['islogin']:
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
    pass

def search(req):
    pass
