# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
import logging
class index(baseAction):
    def __init__(self, pars):
        baseAction.__init__(self, pars)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)
        
    def index(self):
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
