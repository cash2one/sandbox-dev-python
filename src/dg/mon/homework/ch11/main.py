#!\urs\bin\env python
#encoding:utf-8

import urllib
import socket
import hashlib
import codecs
import os
import shutil
import sys
reload(sys)

import util
import parser

sys.setdefaultencoding('utf8')
socket.setdefaulttimeout(10)

html_folder='html'
img_folder='images'

def write_html(path, html):
    m = hashlib.md5()
    m.update(html)
    fn = m.hexdigest()
    # print fn
    filename = os.path.join(path, '%s.html' % fn)
    codecs.open(filename, 'w', 'utf-8').write(html)

if __name__=='__main__':


    pre_url_list = [
        "http://tieba.baidu.com/p/2738151262",
        'http://rrztnn@163.com.home.news.cn/portal/home',
    ]

    post_url_list = []

    count = 0
    util.init_path([html_folder, img_folder])
    
    while pre_url_list and count<100:
        # print 'pre_url_list: %s' % len(pre_url_list)
        # print 'post_url_list: %s' % len(post_url_list)
        url = pre_url_list.pop()
        # print 'current url: %s' % url
        html = util.get_html(url)
        # print 'html => ', html
        if not html:
            continue
        hp = parser.HP(url)
        hp.feed(html)
        hp.close()
        # print hp.links
        for link in hp.links:
            if not link.startswith('http'):
                continue
            if link not in post_url_list and link not in pre_url_list and link!=url and \
                link not in util.exclude_url_list and link not in util.error_url_list:
                pre_url_list.append(link)
        write_html(html_folder, html)
        post_url_list.append(url)
        count+=1
        # print 'url count: %s' % count

