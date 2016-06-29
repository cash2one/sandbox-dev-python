# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
import logging
import control
class user(baseAction):
    def __init__(self, pars):
        baseAction.__init__(self, pars)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)
        
    def register(self):
        method = web.ctx.env.get('REQUEST_METHOD')
        if method=='GET':
            self.assign('status',0)
        else:
            self.assign('status',1)
            pars = self.getPars()
            rt = control.user_register(pars)
            if rt>=1:
                self.assign('msg','恭喜注册完成，请直接登录！')
            elif rt==-1:
                self.assign('msg','密码设置不一致，请重新设置！')
            else:
                self.assign('msg','注册失败，请联系管理员')
        return self.display('user_register')  ##显示指定模板

    def login(self):
        pars = self.getPars()  ##获取请求参数
        rt = control.user_login(pars)
        if rt:
            raise web.seeother('/index/index')
        else:
            self.assign('msg','用户名或密码错误，登录失败！')
            return self.display('user_login')  ##显示指定模板

    def logout(self):
        web.ctx.session.login = False
        web.ctx.session.user_info = {}
        raise web.seeother('/index/index')

    def reset_passwd(self):
        settings = self.getSettings()  ##获取setting对象
        count = settings.WEB_NAME  ##获取具体的setting值
        inputParams = self.getPars()  ##获取请求参数
        tableObj = model.table1()  ##获取数据表对象
        condition = {'1':1}
        print condition
        listData = tableObj.getList('*',condition)  ##进行表查询
        print listData
        self.assign('listData',listData)  ##设置为模板变量
        logging.debug('This is debug message')
        logging.info('This is info message')
        logging.warning('This is warning message')
        return self.display('index')  ##显示指定模板

    def profile(self):
        settings = self.getSettings()  ##获取setting对象
        count = settings.WEB_NAME  ##获取具体的setting值
        inputParams = self.getPars()  ##获取请求参数
        tableObj = model.table1()  ##获取数据表对象
        condition = {'1':1}
        print condition
        listData = tableObj.getList('*',condition)  ##进行表查询
        print listData
        self.assign('listData',listData)  ##设置为模板变量
        logging.debug('This is debug message')
        logging.info('This is info message')
        logging.warning('This is warning message')
        return self.display('index')  ##显示指定模板