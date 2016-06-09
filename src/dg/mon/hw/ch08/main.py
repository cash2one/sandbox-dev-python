#!/usr/bin/python
#encoding:utf-8
# 编写一个方法或类，接受2个参数：fromDict， toDict；功能是把指定格式的数据库转换成另一种格式的数据库；
# fromDict = {'type':'sqlite', 'connect_paramters' : '/path/to/sqlite'}
# toDict = {'type' : 'mysql', 'connect_paramters' : {'host':'localhost', 'username':'', 'password':'', 'port':'3306', 'dnname':'name'}}
# 如：convertDB(fromDict, toDict)则是把指定的sqlite数据库转换到mysql数据库中。至少实现任意2种数据库类型的转换，具体实现方法不限
import re

if __name__ == '__main__':
    pass