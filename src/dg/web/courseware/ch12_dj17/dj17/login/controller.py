#encoding: utf-8
__author__ = 'xwchen2'
from dj17 import function as fun
from models import User

def user_register(pars):
    if pars['passwd']!=pars['repasswd']:
        return -1
    # 数据库操作
    condition = fun.warp_data(pars)
    del condition['repasswd']
    condition['create_date'] = fun.now()
    condition['passwd'] = fun.mk_md5(condition['passwd'])
    # print condition
    u = User(**condition)
    u.save()
    if u.name:
        return 1

def user_login(pars):
    email = pars.get('email')
    passwd = fun.mk_md5(pars.get('passwd'))
    condition = {'email':email}
    try:
        r = User.objects.get(**condition)
        if r and r.passwd==passwd:
            return r
    except:
        return None

