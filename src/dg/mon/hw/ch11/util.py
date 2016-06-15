import os
import shutil
import urllib
import parser

error_url_list = []
exclude_url_list = []

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
        # print 'HTTP MESSAGE: ', obj.info()
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

def get_img(url, filename=None, path=r'images'):
    if not filename:
        filename = url.rsplit('/',1)[1]
    urllib.urlretrieve(url,os.path.join(path, filename))

def init_path(paths):
    for path in paths:
        if os.path.exists(path):
            shutil.rmtree(path)
        os.mkdir(path)