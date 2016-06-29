#encoding: utf-8
__author__ = 'macy'

from login.models import Company, Job, User, Resume, JobApply, JobFeedback
from dj17 import function as fun

def get_company_info(uid):
    try:
        return Company.objects.get(uid=uid)
    except:
        return {}

def insert_company(data):
    c = Company(**data)
    c.save()
    return c.id

def update_company(data):
    r = Company.objects.filter(id=data['id']).update(**data)
    return r

def get_job_info(id):
    try:
        return Job.objects.get(id=id)
    except:
        return {}

def post_job_info(data):
    id = data.pop('id')
    data['cid'] = Company.objects.get(uid=data['uid'])
    data['uid'] = User.objects.get(id=data['uid'])
    if id:  ##更新
        return Job.objects.filter(id=id).update(**data)
    else:
        return Job.objects.create(**data)

def get_job_list(uid):
    return Job.objects.filter(uid=uid)

def get_job_search(keywords):
    return Job.objects.filter(name__contains=keywords)

def job_apply(data):
    if 'job_id' not in data:
        return {'errorCode':-1, 'msg':'job_id should be post'}
    job_id = data.get('job_id')
    uid = Job.objects.get(id=job_id).uid
    send_uid = User.objects.get(id=data.get('send_uid'))
    resume_id = Resume.objects.get(uid=uid).id
    is_read = 0
    create_date = fun.now()
    s = locals()
    del s['data']
    # print s
    j = JobApply.objects.create(**s)
    if j:
        s = {'errorCode':0, 'msg':'你的职位申请已发送成功！', "job_id":job_id}
    else:
        s = {'errorCode':-2, 'msg':'你的职位申请已发送失败！'}
    return s

def send_feedback(data):
    data['uid'] = User.objects.get(id=data['uid'])
    r = JobFeedback.objects.create(**data)
    if r:
        JobApply.objects.filter(send_uid=data['uid'], job_id=data['job_id']).update(is_read=1)
    return r