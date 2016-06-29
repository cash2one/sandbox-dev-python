#!/usr/bin/env python
#coding=utf-8
import os
#网站信息
WEB_URL='/'
WEB_TITLE='拉勾项目'
WEB_NAME='dataguru学习'
WEB_SUBNAME=''
WEB_KEYWORDS=''
WEB_DESCRIPTION=''
TEMPLATE_THEME='default'
PER_PAGE_COUNT = 10

#账号相关
ADMIN_USERNAME = 'five3@163.com'
ADMIN_PASSWORD='chenxiaowu'

#项目配置
DEFAULT_PATH='/index/index'
DEBUG_SWITCH=True

#路径信息
ROOT_PATH=os.getcwd()+'/'
DATA_DIR_PATH=ROOT_PATH+'data/'
TMP_DIR_PATH=ROOT_PATH+'data/cache/'

#目录结构
UPLOAD_DIR='static/upload/'
TPL_DIR = 'templates'

#数据库信息
# DB_TYPE='sqlite'
# DB_STRING=DATA_DIR_PATH+'webpy.db'
# DB_TABEL_PREFIX='webpy_'
DB_TYPE='mysql'
DB_STRING='localhost/3306/root/changeit!/lagou'
DB_TABEL_PREFIX='lagou_'

import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='r')