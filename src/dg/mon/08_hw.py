#!/usr/bin/python
#encoding:utf-8
import re


def foo(xpath, content):
    print xpath
    if xpath.startswith('/'):
        arr= xpath[1:].split('/', 1)
        node = arr[0]
        c = re.compile(r"\<%s\>(.*?)\<\/%s\>" % (node, node), re.S)
        # print c.pattern
        content_list = c.findall(content)
        if len(arr) > 1:
            xpath = '/' + arr[1]
            return foo(xpath, content_list[0].strip())
        else:
            return content_list[0].strip()


s = '''<html>
        <header><title>hello world</title></header>
        <body>
            <div>
                <h1>Hello World</h1>
            </div>
            <div>
                <span>test</span>
            </div>
        </body>
        </html>'''
xpath = '/div'
print foo(xpath, s)