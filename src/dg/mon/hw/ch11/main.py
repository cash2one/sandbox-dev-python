#!\urs\bin\env python
#encoding:utf-8

import urllib
import socket

socket.setdefaulttimeout(10)
exclude_url_list = []
error_url_list = []

def get_html(url):
    proto, rest = urllib.splittype(url)
    res, rest = urllib.splithost(rest)
    if not res:
        print "unkonw url"
        return None
    else:
        if '@' in res:
            print 'SKIP...'
            return None
    try:
        obj = urllib.urlopen(url)
        if obj.getcode() != 200:
            print 'INFO: get html with error code ', obj.getcode()
            error_url_list.append(url)
            return None
        print 'HTTP MESSAGE: ', obj.info()
        if 'text/html' not in obj.info().get('Content-Type'):
            print 'INFO: SKIP for Non-HTML Content'
            exclude_url_list.append(url)
            return None
        html = obj.read()
        for code in ['gbk', 'utf-8', 'base64']:
            if html.decode(code, 'ignore') == html.decode(code, 'replace'):
                return html.decode(code)
        raise UnicodeDecodeError('HTML decoding error!')
    except Exception, e:
        print 'INFO: get HTML failed with URL %s' % url
        print e.message

def get_img(url, filename=None, path=r'D:/temp'):
    import os
    if not filename:
        filename = url.rsplit('/',1)[1]
    urllib.urlretrieve(url,os.path.join(path, filename))


from HTMLParser import HTMLParser
class HP(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "href":
                        self.links.append(value)
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import hashlib
import codecs
import os
import shutil

def write_html(folder, html):
    m = hashlib.md5()
    m.update(html)
    fn = m.hexdigest()
    print fn
    filename = os.path.join(folder, '%s.html' % fn)
    codecs.open(filename, 'w', 'utf-8').write(html)

if __name__=='__main__':


    pre_url_list = [
        "http://tieba.baidu.com/p/2738151262",
        'http://rrztnn@163.com.home.news.cn/portal/home',
    ]

    post_url_list = []

    count = 0
    
    folder='output'
    # os.removedirs(folder)
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    
    while pre_url_list and count<100:
        print 'pre_url_list: %s' % len(pre_url_list)
        print 'post_url_list: %s' % len(post_url_list)
        url = pre_url_list.pop()
        print 'current url: %s' % url
        html = get_html(url)
        print 'html => ', html
        if not html:
            continue
        hp = HP()
        hp.feed(html)
        hp.close()
        print hp.links
        for link in hp.links:
            if not link.startswith('http'):
                continue
            if link not in post_url_list and link not in pre_url_list and link!=url and \
                link not in exclude_url_list and link not in error_url_list:
                pre_url_list.append(link)
        write_html(folder, html)
        post_url_list.append(url)
        count+=1
        print 'url count: %s' % count

