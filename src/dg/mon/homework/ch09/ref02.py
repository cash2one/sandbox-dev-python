#!/bin/python
# __encoding=utf-8__
__author__ = 'kfzx-zhongw'
from xml.etree import ElementTree
from xml.etree.ElementTree import Element


def findelement(root, pattern):
    parentelement = root
    result = root
    if root.tag == pattern.split("/")[1]:
        for keyword in pattern.split("/")[2:]:
            parentelement = result
            result = parentelement.find(keyword)
    return parentelement, result


def findxml(root, pattern):
    parentElement, result = findelement(root, pattern)
    return result


def removexml(root, pattern):
    parentelement, element = findelement(root, pattern)
    parentelement.remove(element)


def appendxml(root, pattern, appendelement):
    parentElement, _ = findelement(root, pattern)
    parentElement.append(appendelement)


inputstring = "<html><header><gdfg>xxxdf</gdfg></header></html>"
pattern = "/html/header/gdfg"

root = ElementTree.fromstring(inputstring)

result = findxml(root, pattern)

removexml(root, pattern)

e = Element('et', {'k1': 'v1', 'k2': 'v2'})
e.text = 'et text'
appendxml(root, pattern, e)

dataxml = ElementTree.tostring(root, encoding='utf-8')

print dataxml



