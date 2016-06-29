#encoding: utf-8
__author__ = 'macy'

from login.models import Company
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

