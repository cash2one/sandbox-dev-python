# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
import control
import logging
class resume(baseAction):
    def __init__(self, pars):
        baseAction.__init__(self, pars)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)

    def default(self):
        if not self.isLogin():
            self.assign('msg', '你当前还没有登录，请先登录！')
            return self.display('msg')
        uid = self.getUid()
        resume_info = model.resume().getOne('*', {'uid':uid})
        if resume_info:
            self.assign('resume_info',resume_info)
            resume_id = resume_info['id']
            work_experience = model.work_experience().getList('*', {'resume_id' : resume_id})
            self.assign('work_experience',work_experience)
            study_experience = model.study_experience().getList('*', {'resume_id' : resume_id})
            self.assign('study_experience',study_experience)
        else:
            self.assign('resume_info',{})
        return self.display('resume')

    def post(self):
        pars = self.getPars()
        pars['uid'] = self.getUid()
        rt = control.resume_post(pars)
        if rt>=1:
            raise web.seeother('/resume/default')
        else:
            self.assign('msg','提交简历失败,请联系管理员！')
            return self.display('msg')

    def work(self):
        pars = self.getPars()
        rt = control.resume_work(pars)
        if rt>=1:
            raise web.seeother('/resume/default')
        else:
            self.assign('msg','提交工作经验失败,请联系管理员！')
            return self.display('msg')

    def study(self):
        pars = self.getPars()
        rt = control.resume_study(pars)
        if rt>=1:
            raise web.seeother('/resume/default')
        else:
            self.assign('msg','提交学习经历失败,请联系管理员！')
            return self.display('msg')

    def search(self):
        pars = self.getPars()
        keywords = pars.get('keywords')
        resume_list = control.resume_search(keywords)
        self.assign('resume_list',resume_list)
        return self.display('resume_list')