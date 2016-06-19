#!/usr/bin/python
#encoding:utf-8
# 编写一个方法或类，接受2个参数：fromDict， toDict；功能是把指定格式的数据库转换成另一种格式的数据库；
# fromDict = {'type':'sqlite', 'connect_paramters' : '/path/to/sqlite'}
# toDict = {'type' : 'mysql', 'connect_paramters' : {'host':'localhost', 'username':'', 'password':'', 'port':'3306', 'dnname':'name'}}
# 如：convertDB(fromDict, toDict)则是把指定的sqlite数据库转换到mysql数据库中。至少实现任意2种数据库类型的转换，具体实现方法不限
import re
import sqlite3_module
import mysql_module
import os


def extract_data(fromDict):
    if fromDict['type'] == 'sqlite':
        sqlite_filepath = fromDict['connect_paramters']
        result = sqlite3_module.extract_data(sqlite_filepath)
    elif fromDict['type'] == 'mysql':
        result = mysql_module.extract_data(fromDict['connect_paramters'])
    return(result)


def load_data(toDict, statments):
    if toDict['type'] == 'sqlite':
        sqlite_filepath = toDict['connect_paramters']
        sqlite3_module.load_data(sqlite_filepath, statments)
    elif toDict['type'] == 'mysql':
        mysql_module.load_data(toDict['connect_paramters'], statments)


def etl_data(fromDict, toDict):
    
    # reset test data
    if fromDict['type'] == 'sqlite':
        sqlite_filepath = fromDict['connect_paramters']
        sqlite3_module.remove_file(sqlite_filepath)
        sqlite3_module.write(sqlite_filepath)
    if toDict['type'] == 'sqlite':
        sqlite_filepath = toDict['connect_paramters']
        if os.path.exists(sqlite_filepath):
            raise Exception('etl target {0} is exists!!!'.format(sqlite_filepath))
    if toDict['type'] == 'mysql':
        if mysql_module.check_database_exists(toDict['connect_paramters']):
            raise Exception("etl target {0} is exists!!!".format(toDict['connect_paramters']['dbname']))
    
    extract_statments = extract_data(fromDict)
    # print(extract_statments)
    load_data(toDict, extract_statments)

if __name__ == '__main__':
    
    # Test #1 sqlite => sqlite
    fromDict = {'type': 'sqlite', 'connect_paramters': 'from.sqlite3'}
    toDict = {'type': 'sqlite', 'connect_paramters': 'to.sqlite3'}
    # Test #2 sqlite => mysql
    # fromDict = {'type': 'sqlite', 'connect_paramters': 'from.sqlite3'}
    # toDict = {'type' : 'mysql', 'connect_paramters' : {'host':'localhost', 'username':'root', 'password':'mysql', 'port':'3306', 'dbname':'test'}}
    # Test #3 mysql => mysql
    # fromDict = {'type' : 'mysql', 'connect_paramters' : {'host':'localhost', 'username':'root', 'password':'mysql', 'port':'3306', 'dbname':'test'}}
    # toDict = {'type' : 'mysql', 'connect_paramters' : {'host':'localhost', 'username':'root', 'password':'mysql', 'port':'3306', 'dbname':'test1'}}
    # Test #4 mysql => sqlite
    # fromDict = {'type' : 'mysql', 'connect_paramters' : {'host':'localhost', 'username':'root', 'password':'mysql', 'port':'3306', 'dbname':'test'}}
    # toDict = {'type': 'sqlite', 'connect_paramters': 'to.sqlite3'}
    
    etl_data(fromDict, toDict);
    