# -*- coding: utf-8 -*-
#!/usr/bin/env python
import model
import web
def group_info(gid):
    tableObj = model.groups()  ##获取数据表对象
    g_info = tableObj.getOne('id,name,description', {'id':gid})  ##进行表查询
    tableObj = model.query()  ##获取数据表对象
    f_list = tableObj.fetchAll('select forum.id,forum.title from forum,group_forum gf where gf.gid=%s and gf.fid=forum.id' % gid)  ##进行表查询
    return g_info,f_list

def gourp_new(pars):
    tableObj = model.groups()  ##获取数据表对象
    condition = dict(pars)
    user_info = web.ctx.session.user_info
    if user_info:
        condition['owner'] = user_info['id']
    else:
        return  -1
    print condition
    return tableObj.insert(condition)
