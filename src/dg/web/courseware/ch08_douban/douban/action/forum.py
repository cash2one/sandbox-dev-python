# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
import control
import logging
class forum(baseAction):
    def __init__(self, pars):
        baseAction.__init__(self, pars)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)

    def view(self):
        inputParams = self.getPars()  ##获取请求参数
        fid = inputParams.get('id')
        f_info = control.forum_info(fid)
        self.assign('f_info',f_info[0])
        self.assign('reply',f_info[1])
        return self.display('forum_view')

    def new(self):
        inputParams = self.getPars()
        if self.getMethod()=='GET':
            self.assign('gid',inputParams.get('gid'))
            return self.display('forum_new')
        else:
            rt = control.forum_new(inputParams)
            if rt>=1:
                self.assign('msg','恭喜，发帖成功！')
            elif rt==-1:
                self.assign('msg','您当前未登录，请先登录')
            else:
                self.assign('msg','发帖失败，请联系管理员')
            return self.display('msg')  ##显示指定模板
