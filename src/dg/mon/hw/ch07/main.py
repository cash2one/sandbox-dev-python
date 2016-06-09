#!/bin/python
#__encoding=utf-8__
import codecs
import re
from lxml import etree

if __name__ == '__main__':

    f = codecs.open("test.html", "r", "utf-8")
    content = f.read()
    f.close()
    tree = etree.HTML(content)

    block_pattern = re.compile(u"<h3>(.*?)</h3>", re.I | re.S)
    m = block_pattern.findall(content)
    item_pattern = re.compile(u"<li>(.*?)</li>", re.I | re.S)
    items = item_pattern.findall(m[0])
    for i in items:
        print i

    nodes = tree.xpath("/descendant::ul[@id='id1']")

    childNodes = nodes[0].xpath("li/a")
    for n in childNodes:
        print n.text
