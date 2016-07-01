# -*- coding: utf-8 -*-

import re


raw = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<h1>我的第一个标题</h1>

<p>我的第一个段落。</p>

</body>
</html>

"""
tags = "/html/head/title".split("/")[1:]


def html_parse(html, tags):
    if len(tags) > 0:
        regex_str = r"[\s\S]*<"+tags[0]+">([\s\S]*)</"+tags[0]+">[\s\S]*"
        regex = re.compile(regex_str, re.I)
        s = regex.match(html)
        html_parse(s.expand(r'\1'), tags[1:])
    else:
        print html

html_parse(raw, tags)