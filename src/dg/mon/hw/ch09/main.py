#!/usr/bin/python
# encoding:utf-8

import sys
import xml.etree.ElementTree as eTree
import xml.etree.ElementTree as ElementTree
import xml2dict


def test1():
    tree = eTree.parse('doc.xml')
    root = tree.getroot()
    print("============ initial xml ============")
    for elem in tree.iterfind('branch/sub-branch'):
        print(elem.tag)
        print(elem.attrib)
    print("============ append node ============")
    for elem in tree.iterfind('branch/sub-branch/..'):
        elem.append(eTree.Element("sub-branch", attrib={"new": "subrelease02"}))
    print("============ new xml ============")
    for elem in tree.iterfind('branch/sub-branch'):
        print(elem.tag)
        print(elem.attrib)
    print("============ remove node ============")
    for elem in tree.iterfind('branch/sub-branch/..'):
        for child in elem.getchildren():
            if "new" in child.attrib:
                elem.remove(child)
    print("============ new xml ============")
    for elem in tree.iterfind('branch/sub-branch'):
        print(elem.tag)
        print(elem.attrib)


def test2():
    tree = ElementTree.parse('doc.xml')

    root = tree.getroot()

    xmldict = xml2dict.XmlDictConfig(root)
    print("============ initial xml ============")
    print(xmldict)
    print("============ search xml by xpath ============")
    print(xpath_get(xmldict, "branch/sub-branch"))

    print("============ append node ============")
    for elem in tree.iterfind('branch/sub-branch/..'):
        elem.append(eTree.Element("sub-branch2", attrib={"new": "subrelease02"}))
    print(xml2dict.XmlDictConfig(root))

    print("============ remove node ============")
    for elem in tree.iterfind('branch/sub-branch/..'):
        for child in elem.getchildren():
            if "new" in child.attrib:
                elem.remove(child)
    print(xml2dict.XmlDictConfig(root))


def xpath_get(mydict, path):
    elem = mydict
    try:
        for x in path.strip("/").split("/"):
            elem = elem.get(x)
    except:
        pass
    return elem


if __name__ == "__main__":
    # test1()
    test2()



