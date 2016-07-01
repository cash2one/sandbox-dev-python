# encoding:utf-8

import sqlite3, MySQLdb

def convertDB(fromDict, toDict):
    fromType = fromDict.get("type")
    fromParam = fromDict.get("connect_parameters")
    toType = toDict.get("type")
    toParam = toDict.get("connect_parameters")

    if fromType=="sqlite" and toType=="mysql":
        # 连接sqlite
        litConn = sqlite3.connect(fromParam)
        # 连接mysql
        myConn = MySQLdb.connect(host=toParam.get("host"), user=toParam.get("username"), passwd=toParam.get("password"), port=int(toParam.get("port")), db=toParam.get("dbname"))
        tabs = litConn.execute("select name,sql from sqlite_master where type='table'").fetchall()
        for tab in tabs:
            t, sqlCreate = tab              # sqlite的表名和建表语句
            print sqlCreate                 # 打印建表语句
            myConn.query(sqlCreate)         # mysql建表
            data = litConn.execute("select * from %s" % t).fetchall()   # 查看sqlite表数据
            for row in data:
                rowData = str(row).replace('u','')      # 将set转成字符串，并将u替换掉
                sqlInsert = "insert into %s values %s" % (t, rowData)
                print sqlInsert                         # 打印插入数据语句
                myConn.query(sqlInsert)                 # 将数据插入mysql
                myConn.commit()
        myConn.close()
        litConn.close()


fromDict = {'type':'sqlite', 'connect_parameters':'E:\\test'}
toDict = {'type':'mysql', 'connect_parameters':{'host':'localhost','username':'root','password':'root','port':'3306','dbname':'test'}}
convertDB(fromDict, toDict)





#encoding=utf-8
import mysql.connector
import sqlite3,re,copy
from mysql.connector import errorcode
#数据库名
global DB_NAME,TABLES
DB_NAME = ''
#表结构,没用到
TABLES = {}

def convertDB(fromDict, toDict):
	"""

	:rtype: 字符串
	"""
	#连接源数据库
	if fromDict['type'] == 'sqlite':
		conn = sqlite3.connect(fromDict['connect_paramters'])
#		print fromDict['connect_paramters']
		curr = conn.cursor()
	elif fromDict['type'] == 'mysql':
		conndict = fromDict['connect_paramters']
		conn = mysql.connector.connect(**conndict)
		curr = conn.cursor()
	#建目标数据库
	if toDict['type'] == 'sqlite':
		conn1 = sqlite3.connect(fromDict['connect_paramters'])
#		print toDict['connect_paramters']
		curr1 = conn1.cursor()
	elif toDict['type'] == 'mysql':
		conndict = toDict['connect_paramters']
		DB_NAME = conndict['database']
		del conndict['database']
		conn1 = mysql.connector.connect(**conndict)
		cursor = conn1.cursor()
		try:
			conn1.database = DB_NAME
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_BAD_DB_ERROR:
				create_database(cursor,DB_NAME)
				conn1.database = DB_NAME
			else:
				print(err)
				exit(1)
		curr1 = conn1.cursor()
	#读取源表，只做了sqlite
	curr.execute('''select name from sqlite_master where type='table' order by name;''')
	ctable = curr.fetchall()
	for i in ctable:
		curr.execute("PRAGMA table_info(%s)" %i)
		ctableinfo = curr.fetchall()
		sqltable = "CREATE TABLE %s ("%i
		sqldata = "INSERT INTO %s ("%i
		num = len(ctableinfo)
		for ii in ctableinfo:
			num = num -1
			for sub in range(1,len(ii)):
				if sub == 1:
					sqltable = sqltable + str(ii[sub])+' '
					if num >0:
						sqldata =  sqldata + str(ii[sub])+','
					else:
						sqldata =  sqldata + str(ii[sub])+')'
				elif  sub == 2 :
					if ii[sub] == 'REAL':
						sqltable = sqltable + 'DOUBLE '
					else:
						sqltable = sqltable + str(ii[sub])+' '
				elif sub == 3 :
					if ii[sub] == 1:
						sqltable = sqltable + 'NOT NULL '
				elif sub == 5 :
					if ii[sub] == 1:
						sqltable = sqltable + 'PRIMARY KEY '
			if num>0:
				sqltable = sqltable + ','
			else:
				sqltable = sqltable + ')'
			#print sqldata
			#print sqltable 表结构导入
		curr1.execute(sqltable)
		curr.execute("select * from %s " %i)
		cdata = curr.fetchall()
		print "这是源数据：",
		print(cdata)
		sqldata = "%s VALUES (%s%%s)" %(sqldata,(len(ii)-2)*'%s,')

		#print sqldata
		curr1.executemany(sqldata,cdata)
		conn1.commit()
	conn.close()
	conn1.close()


def create_database(cursor,database):
	try:
		cursor.execute("CREATE DATABASE {}".format(database))
	except mysql.connector.Error as err:
		print("Failed creating database: {}".format(err))
		exit(1)

souredict= dict(type='sqlite', connect_paramters='test1.db')
targetdict= dict(type='mysql',
				 connect_paramters=dict(host='localhost', user='root', passwd='abcd1234', port='3306',
										database='test1'))

cover = convertDB(souredict,targetdict)



#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:lanjuuff
# date:201605**
# function:不同库数据同步,已实现mysql、redis、mongodb.中间结果集为字典构成的元组.

import MySQLdb
import time
import redis
import pymongo


class DB(object):
    def __init__(self, host=None, port=None, db=None):
        self.__host = host
        self.__port = port
        self.__db = db
        self.conn = None

    def connect(self, *args, **kwargs):
        return self.conn

    def disconnect(self, *args, **kwargs):
        self.conn = None

    def get_data(self, *args, **kwargs):
        """
            返回值为字典的元组
        """
        pass

    def insert_data(self, *args, **kwargs):
        """
            插入数据
        """
        pass

    def clear_data(self, *args, **kwargs):
        """
            清空数据
        """
        pass


class MysqlDB(DB):
    def __init__(self, host=None, port=None, user=None, password=None, db=None):
        # super(MysqlDB, self).__init__(host, port, db)
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__db = db
        self.conn = None

    def connect(self, host=None, port=None, user=None, password=None, db=None):
        if host:
            self.__host = host
        if port:
            self.__port = port
        if user:
            self.__user = user
        if password:
            self.__password = password
        if db:
            self.__db = db
        try:
            self.conn = MySQLdb.connect(host=self.__host, port=self.__port, user=self.__user, passwd=self.__password,
                                        db=self.__db)
        except Exception, e:
            print "--[FAIL][%s] Connect to mysql host:%s,port:%s,user:%s,password:%s failed. Detail:%s" % \
                  (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.__host, self.__port, self.__user,
                   self.__password, e)
            return None
        return self.conn

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def get_data(self, args):
        tab = args[0]
        cols_tup = args[1]
        cols_type = args[2]
        cnt = 0
        # result = None
        result_temp = None
        cur = self.conn.cursor()
        sql = 'select * from %s' % tab
        try:
            cnt = cur.execute(sql)
            result_temp = cur.fetchall()
        except Exception, e:
            print "--[FAIL][%s] Execute sql: %s failed. detail:%s" % \
                  (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), sql, e)
        finally:
            cur.close()
        if result_temp:
            result = [dict(zip(cols_tup, row)) for row in result_temp]
            for i, col_type in enumerate(cols_type):
                if col_type == 'date':
                    j = cols_tup[i]
                    for row in result:
                        row[j] = row[j].strftime('%Y-%m-%d %H:%M:%S')
            print 'get %d rows' % cnt
            return tuple(result)
        else:
            return None

    def insert_data(self, data, args):
        tab = args[0]
        cols_tup = args[1]
        cols_type = args[2]
        cur = self.conn.cursor()
        cnt = 0
        sql = None
        try:
            for row in data:
                col_str = val_str = None
                for key, val in row.items():
                    if col_str:
                        col_str = '%s, %s' % (col_str, key)
                    else:
                        col_str = '%s' % key
                    col_type = cols_type[cols_tup.index(key)]
                    if val == 'None' or not val:
                        val = 'NULL'
                    if col_type == 'number':
                        val = val
                    else:
                        val = "'%s'" % val
                    if val_str:
                        val_str = "%s, %s" % (val_str, val)
                    else:
                        val_str = "%s" % val
                sql = 'insert into %s (%s) values (%s)' % (tab, col_str, val_str)
                cnt += cur.execute(sql)
            self.conn.commit()
        except Exception, e:
            print "--[FAIL][%s] Execute sql: %s failed. detail:%s" % \
                  (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), sql, e)
        finally:
            cur.close()
            cnt = 0
        print 'insert %d records.' % cnt
        return cnt

    def clear_data(self, args):
        tab = args[0]
        cnt = None
        sql = 'delete from %s' % tab
        cur = self.conn.cursor()
        try:
            cnt = cur.execute(sql)
            self.conn.commit()
        except Exception, e:
            print "--[FAIL][%s] Execute sql: %s failed. detail:%s" % \
                  (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), sql, e)
        finally:
            cur.close()
        return cnt


class RedisDB(DB):
    def __init__(self, host=None, port=None, db=None, password=None):
        # super(RedisDB, self).__init__(host, port, db)
        self.__host = host
        self.__port = port
        self.__db = db
        self.__password = password
        self.conn = None

    def connect(self, host=None, port=None, db=None, password=None):
        if host:
            self.__host = host
        if port:
            self.__port = port
        if db is not None:
            self.__db = db
        if password is not None:
            self.__password = password
        self.conn = redis.StrictRedis(host=self.__host, port=self.__port, db=self.__db, password= self.__password)
        return self.conn

    def disconnect(self):
        if self.conn:
            self.conn = None

    def get_data(self, args):
        name_prefix = args[0]
        cols_tup = args[1]
        cols_type = args[2]
        primary_key = args[3]
        result = []
        cnt = 0
        names = self.conn.keys('%s:*' % name_prefix)
        cnt = len(names)
        for name in names:
            rec = self.conn.hgetall(name)
            rec[primary_key] = name.lstrip('%s:' % name_prefix)
            for k, v in rec.iteritems():
                if v == 'None' or v == '':
                    v = None
                else:
                    col_type = cols_tup[cols_tup.index(k)]
                    if col_type == 'number':
                        try:
                            rec[k] = int(v)
                        except TypeError:
                            rec[k] = float(v)
            result.append(rec)
        print 'get %d keys.' % cnt
        return tuple(result)

    def insert_data(self, data, args):
        name_prefix = args[0]
        primary_key = args[3]
        cnt = 0
        for rec in data:
            name = '%s:%s' % (name_prefix, rec[primary_key])
            cnt_temp = 0
            for k, v in rec.iteritems():
                if k != primary_key:
                    cnt_temp += self.conn.hset(name, k, v)
            if cnt_temp:
                cnt += 1
        print 'hset %d keys.' % cnt
        return cnt

    def clear_data(self, args):
        name_prefix = args[0]
        cnt = 0
        names = self.conn.keys('%s:*' % name_prefix)
        for name in names:
            cnt += self.conn.delete(name)
        print 'delete %d keys.' % cnt
        return cnt

class MongoDB(DB):
    def __init__(self, host=None, port=None):
        # super(RedisDB, self).__init__(host, port, db)
        self.__host = host
        self.__port = port
        self.conn = None

    def connect(self, host=None, port=None):
        if host:
            self.__host = host
        if port:
            self.__port = port
        self.conn = pymongo.MongoClient(host=self.__host, port=self.__port)

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def get_data(self, args):
        collection = args[0]
        db = args[4]
        cnt = 0
        result = None
        my_collection = self.conn.get_database(db).get_collection(collection)
        result = my_collection.find({}, {"_id":0})
        result = tuple(result)
        cnt = len(result)
        print 'get %d rows' % cnt
        return tuple(result)


    def insert_data(self, data, args):
        collection = args[0]
        db = args[4]
        obj_list = None
        cnt = 0
        my_collection = self.conn.get_database(db).get_collection(collection)
        obj_list = my_collection.insert(data)
        cnt = len(obj_list)
        print 'insert %d documents.' % cnt
        return cnt

    def clear_data(self, args):
        collection = args[0]
        db = args[4]
        my_collection = self.conn.get_database(db).get_collection(collection)
        result = my_collection.delete_many({})
        print 'delete %d documents.' % result.deleted_count
        # print result.raw_result
        return result.deleted_count

def format_print(rows):
    for i, row in enumerate(rows):
        print '\t%2d:\t%s' % (i, row)
    print '\tcount: %d' % len(rows)
    print '*' * 100
    print


def transferdb(sourcedb, args1, targetdb, args2, clear_data=False):
    cnt = 0
    sourcedb.connect()
    targetdb.connect()
    print 'source database:'
    data = sourcedb.get_data(args1)
    format_print(data)
    sourcedb.disconnect()
    print 'target database(begin):'
    targetdb_data_before = targetdb.get_data(args2)
    format_print(targetdb_data_before)
    print 'transfering:'
    if data:
        if clear_data:
            targetdb.clear_data(args2)
        targetdb.insert_data(data, args2)
    print '*' * 100, '\n'
    print 'target database(end):'
    targetdb_data_after = targetdb.get_data(args2)
    format_print(targetdb_data_after)
    targetdb.disconnect()
    return cnt


def main():
    tab = name_prefix = collection = 'emp'
    cols_tup = ('empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno')
    cols_type = ('number', 'varchar', 'varchar', 'number', 'date', 'number', 'number', 'number')
    primary_key = 'empno'
    mongo_db = 'test'
    db1 = MysqlDB(host='192.168.239.81', port=3306, user='root', password='root', db='test')
    db2 = RedisDB(host='192.168.239.82', port=6379, db=0)
    db3 = MongoDB(host='192.168.239.82', port=27017)
    db1_args = (tab, cols_tup, cols_type, primary_key)
    db2_args = (name_prefix, cols_tup, cols_type, primary_key)
    db3_args = (collection, cols_tup, cols_type, primary_key, mongo_db)
    transferdb(db1, db1_args, db2, db2_args, clear_data=True)
    print '#' * 100
    print '#' * 100, '\n'
    transferdb(db2, db2_args, db3, db3_args, clear_data=True)


if __name__ == '__main__':
    main()



