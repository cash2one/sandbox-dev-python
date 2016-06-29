# -*- coding: utf-8 -*-
#!/usr/bin/env python
import model
import web

def resume_post(pars):
    print pars
    pars = dict(pars)
    id = pars.pop('id')
    if id=='0':
        return model.resume().insert(pars)
    else:
        return model.resume().update(pars, {'id':id})

def resume_work(pars):
    pars = dict(pars)
    id = pars.pop('id')
    if id=='0':
        return model.work_experience().insert(pars)
    else:
        return model.work_experience().update(pars, {'id':id})

def resume_study(pars):
    pars = dict(pars)
    id = pars.pop('id')
    if id=='0':
        return model.study_experience().insert(pars)
    else:
        return model.study_experience().update(pars, {'id':id})

def resume_search(pars):
    sql = u'select * from resume where hope_work like "%%%s%%"' % pars
    return model.resume().fetchAll(sql)