#encoding: utf-8
__author__ = 'xwchen2'

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

import controller
from dj17 import function as fun

def login(req):
    msg = 'login page'
    if req.method == 'GET':
        msg = '你提交的方式非法！'
        return render_to_response('msg.html', locals())

    data = fun.warp_data(req.POST)
    rt = controller.user_login(data)
    # print rt.id
    if rt:
        req.session['islogin'] = True
        user_info = {}
        user_info['id'] = rt.id
        user_info['name'] = rt.name
        user_info['email'] = rt.email
        req.session['user_info'] = user_info
        return HttpResponseRedirect('/')
    else:
        msg = '用户名或密码错误，登录失败！'
        return render_to_response('msg.html', locals())

def logout(req):
    msg = 'logout page'
    req.session['islogin'] = False
    req.session['user_info'] = {}
    return HttpResponseRedirect('/')

def register(req):
    msg = 'register page'
    if req.method == 'GET':
        status = False
        return render_to_response('user_register.html', locals())
    else:
        status = True
        data = req.POST
        rt = controller.user_register(data)
        if rt>=1:
            msg = '恭喜注册完成，请直接登录！'
        elif rt==-1:
            msg = '密码设置不一致，请重新设置！'
        else:
            msg = '注册失败，请联系管理员'
    return render_to_response('user_register.html', locals())

