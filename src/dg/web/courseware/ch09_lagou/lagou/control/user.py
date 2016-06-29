# -*- coding: utf-8 -*-
#!/usr/bin/env python
import model
import utils.function as fun
import web
def user_register(pars):
    if pars['passwd']!=pars['repasswd']:
        return -1
    # 数据库操作
    tableObj = model.user()  ##获取数据表对象
    condition = dict(pars)
    del condition['repasswd']
    condition['create_date'] = 'now()'
    condition['passwd'] = fun.mk_md5(condition['passwd'])
    listData = tableObj.insert(condition)
    print 'DB Logging:', listData
    return  listData

def user_login(pars):
    email = pars.get('email')
    passwd = fun.mk_md5(pars.get('passwd'))
    tableObj = model.user()  ##获取数据表对象
    condition = {'email':email}
    listData = tableObj.getOne('*',condition)  ##进行表查询
    print listData
    if listData and listData['passwd']==passwd:
        web.ctx.session.login = True
        web.ctx.session.user_info = listData
        return True
    else:
        return None