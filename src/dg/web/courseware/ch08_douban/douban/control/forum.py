# -*- coding: utf-8 -*-
#!/usr/bin/env python
import model
import web
def forum_info(fid):
    tableObj = model.forum()  ##获取数据表对象
    f_info = tableObj.getOne('title, content', {'id':fid})  ##进行表查询
    tableObj = model.query()  ##获取数据表对象
    reply = tableObj.fetchAll('select content,parent_content from reply where fid=%s' % fid)  ##进行表查询
    return f_info,reply

def forum_new(pars):
    condition = dict(pars)
    user_info = web.ctx.session.user_info
    if user_info:
        condition['owner'] = user_info['id']
    else:
        return  -1
    gid = condition.pop('gid')
    if not gid:
        return -2
    tableObj = model.forum()
    rt1 = tableObj.insert(condition)
    print rt1
    tableObj = model.group_forum()
    condition = {'fid':rt1, 'gid':gid}
    rt2 = tableObj.insert(condition)
    if rt1 and rt2:
        return 1
    else:
        return 0
