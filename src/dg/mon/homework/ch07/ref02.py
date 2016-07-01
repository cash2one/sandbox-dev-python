#!/bin/python
# __encoding=utf-8__
__author__ = 'kfzx-zhongw'
import re

pattern = "/html/header"
inputs = ["<html><header><gdfg>xxxdf</gdfg></header></html>", ]
result = ""

print result

re_patterns = [re.compile(r"<" + keyword + ">(.*)</" + keyword + ">", )
               for keyword in pattern.split("/")[1:]]

# print re_patterns
for re_pattern in re_patterns:
    inputs = [re_pattern.findall(i) for i in inputs][0]

print inputs