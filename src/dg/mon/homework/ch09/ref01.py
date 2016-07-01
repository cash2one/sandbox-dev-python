# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 10:00:36 2016

@author: AO
"""

##封装一个xml类，能够通过xpath路径来查找、添加、删除元素节点，
##获取、添加的xml节点对象均为其原生对象。

from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element
import re
 
class MyXml():
    '''xpaht,like:/python/node1/node2/node3'''
    
    def __init__(self,file):
        self.tree=ET.parse(file)
        self.root=self.tree.getroot()
        
    def get_node_with_xpath(self,xpath):
        '''xpaht,like:
        /python/node1/node2/node3
        /python/node1[1]/node2/node3'''
        xpath_list=xpath.lstrip('/').split('/')
        #先判断root节点是否匹配，若不匹配，返回空
        firstnode=xpath_list.pop(0)
        if firstnode<>self.root.tag:
            return None
        elif firstnode==self.root.tag and not xpath_list:
            return self.root
        else:
            #分割节点名，和节点索引，如有索引，假定从0开始
            pattern=re.compile('^(.+)[(d+)]$')
            #初始父节点是root节点
            parent_node=self.root
            while xpath_list:
                nodename=xpath_list.pop(0)
                m=re.match(pattern,nodename)
                #index--取nodename中第index个节点，如没有指定，默认取第一个(index=0)
                if m:
                    nodename,index=m.groups()
                    index=int(index)
                else:
                    nodename,index=nodename,0
                #从父节点找出所有nodename子节点
                tmp_list=parent_node.findall(nodename)
                #tmp_list没有index索引项，则不存在这样的节点，返回空
                if len(tmp_list)<index+1:
                    return None
                else:
                    if xpath_list:
                        #查找节点列表还不为空，则将查出的节点作为父节点继续循环
                        parent_node=tmp_list[index]
                    else:
                        #查找节点列表已为空，则查出的节点即位目标节点
                        return tmp_list[index]

    def add_child_node_by_xpath(self,path,element):
        node=self.get_node_with_xpath(path)
#        if not node:
#            print "not exist the node",path
#        else:
#            node.append(element)
        if node is not None:
            node.append(element)
        else:
            print "not exist the node",path

    def delete_node_by_xpath(self,path):
        parent_node=path[:path.rfind('/')]
        if not parent_node:
            print "path",path,"is root node,can't be deleted"
        else:
            node=self.get_node_with_xpath(path)
#            if not node:
#                print "not exist the path",path
#            else:
#                parent_node=self.get_node_with_xpath(parent_node)
#                parent_node.remove(node)
            if node is not None:
                parent_node=self.get_node_with_xpath(parent_node)
                parent_node.remove(node)
            else:
                print "not exist the path",path
            
        
      

if __name__ == "__main__":                
    test=MyXml(r'e:/xml.txt')   
    print "原始xml:"
    root=test.root
    print ET.tostring(root)
    print "查找"        
    print test.get_node_with_xpath('/python/node1/node2/node3').text            
    print test.get_node_with_xpath('/python/node1[1]/node2/node3').text 
    print test.get_node_with_xpath('python')  
    
    print "添加节点"
    e = Element('et', {'k1', 'v1'})
    e.text = 'et text'
    
    test.add_child_node_by_xpath('/python/node1[1]',e)
    print list(test.get_node_with_xpath('/python/node1[1]'))
    
    print "删除节点"
    test.delete_node_by_xpath('/python/node1[1]/et')
    print list(test.get_node_with_xpath('/python/node1[1]'))
#运行结果    
#原始xml:
#<python name="test" pythonAtt="dataguru">
#        <normal>&#25991;&#26412;&#20869;&#23481;</normal>
#        <cdatatext>sdjfsljf!@#!@3`1`12`2&lt;&gt;&lt;</cdatatext>
#        <node1>
#                <node2>
#                        <node3>test111</node3>
#                </node2>
#        </node1>
#        <node1>
#                <node2>
#                        <node3>test2222</node3>
#                </node2>
#        </node1>
#</python>
#查找
#test111
#test2222
#<Element 'python' at 0xa0a0cf8>
#添加节点
#[<Element 'node2' at 0xa0c5f28>, <Element 'et' at 0xa0a0ba8>]
#删除节点
#[<Element 'node2' at 0xa0c5f28>]



