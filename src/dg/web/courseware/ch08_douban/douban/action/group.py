# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
import control
import logging
class group(baseAction):
    def __init__(self, pars):
        baseAction.__init__(self, pars)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)

    def list(self):
        tableObj = model.groups()  ##获取数据表对象
        listData = tableObj.getList('*')  ##进行表查询
        self.assign('groups',listData)  ##设置为模板变量
        return self.display('group_list')  ##显示指定模板

    def view(self):
        inputParams = self.getPars()
        gid = inputParams.get('id')
        group_info = control.group_info(gid)
        self.assign('group_info',group_info[0])
        self.assign('forum_list',group_info[1])
        return self.display('group_view')  ##显示指定模板

    def new(self):
        if self.getMethod()=='GET':
            return self.display('group_new')
        else:
            inputParams = self.getPars()  ##获取请求参数
            rt = control.gourp_new(inputParams)
            if rt>=1:
                self.assign('msg','恭喜，创建小组成功！')
            elif rt==-1:
                self.assign('msg','您当前未登录，请先登录')
            else:
                self.assign('msg','创建小组失败，请联系管理员')
            return self.display('msg')  ##显示指定模板

    def update(self):
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

    def drop(self):
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

